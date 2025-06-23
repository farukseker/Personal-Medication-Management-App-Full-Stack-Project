import { useCookie } from '#app'
import { useColorMode } from '#imports'


export const useTheme = () => {
    const themeCookieOptions = {
        maxAge: 60 * 60 * 24 * 30 * 6, // 6 ay (saniye cinsinden)
        sameSite: 'lax',
        secure: true,
        path: '/',
    }

    const cookie = useCookie('theme', {
        ...themeCookieOptions,
        default: () => 'system',
    })

    const applyTheme = (newTheme) => {
        const colorMode = useColorMode()
        document.documentElement.setAttribute('class', newTheme)
        document.documentElement.setAttribute('data-theme', newTheme)
        cookie.value = newTheme
        colorMode.preference = newTheme
    }

    return {
        theme: cookie,
        applyTheme,
    }
}
