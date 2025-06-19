import { useLocaleRouter } from '~/composables/useLocaleRouter'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const accessToken = useCookie('access_token', {
      maxAge: 60 * 60 * 24 * 30,
      sameSite: 'lax',   // CSRF dostu
      secure:  true,     // prod’da HTTPS şart
      path:    '/',      // tüm route'larda erişilsin
  })
  const refreshToken = useCookie('refresh_token',{
    maxAge: 60 * 60 * 24 * 30 * 6, // 6 ay mesela
    sameSite: 'lax',
    secure:  true,
    path:    '/',
  })

  const api = $fetch.create({
    baseURL: config.public.API_HOST,
    retryStatusCodes: [401],
    retry: 1,
    async onRequest({ options }) {
      if (accessToken.value) {
        options.headers = {
          ...options.headers,
          Authorization: `Bearer ${accessToken.value}`
        }
      }
    },

    async onResponseError({ response, request, options }) {
      if (response.status === 401 && refreshToken.value) {
        try {
          const tokens = await $fetch('/auth/token/refresh/', {
            method: 'POST',
            baseURL: config.public.API_HOST,
            body: {
              refresh: refreshToken.value
            }
          })
          accessToken.value = tokens.access
          options.headers['Authorization'] = `Bearer ${tokens.access}`
        } catch (err) {
          console.error('Token refresh failed', err)
          // throw err
        }
      }
      // refresh tokeni olmaması durumunda auth var sayılamaz
      else if (response.status === 401) {
        const { go } = useLocaleRouter()
        go('/auth/login')
      }
      // throw response || new Error('API error')
    }
  })

  nuxtApp.provide('api', api)
})
