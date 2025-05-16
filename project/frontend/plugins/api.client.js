export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const accessToken = useCookie('access_token')
  const refreshToken = useCookie('refresh_token')

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

          // Yeni access token'ı cookie'ye yaz
          accessToken.value = tokens.access
          // options.headers.set('Authorization', `Bearer ${tokens.access}`)
          options.headers['Authorization'] = `Bearer ${tokens.access}`
          // Yeni header'la tekrar dene
          // return await $fetch.raw(request, {
          //   ...options,
          //   headers: {
          //     ...options.headers,
          //     Authorization: `Bearer ${tokens.access}`
          //   }
          // })
        } catch (err) {
          console.error('Token refresh failed', err)
          // throw err
        }
      }
      // refresh tokeni olmaması durumunda auth var sayılamaz
      else {
        // const router = useRouter()
        // router.push('/auth/login')
      }
      // throw response || new Error('API error')
    }
  })

  nuxtApp.provide('api', api)
})
