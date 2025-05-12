export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()

  const accessToken = useCookie('access_token')
  const refreshToken = useCookie('refresh_token')

  const api = $fetch.create({
    baseURL: config.public.API_HOST,

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
          const tokens = await $fetch('/auth/refresh', {
            method: 'POST',
            baseURL: config.public.API_HOST,
            body: {
              refresh_token: refreshToken.value
            }
          })

          accessToken.value = tokens.access_token
          refreshToken.value = tokens.refresh_token

          // retry original request
          return await $fetch.raw(request, {
            ...options,
            headers: {
              ...options.headers,
              Authorization: `Bearer ${tokens.access_token}`
            }
          })
        } catch (err) {
          accessToken.value = null
          refreshToken.value = null
          throw err
        }
      }

      throw response._data || new Error('API error')
    }
  })

  nuxtApp.provide('api', api)
})
