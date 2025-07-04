import { defineStore } from 'pinia'
import { useColorMode, useCookie } from '#imports'
export const useThemeStore = defineStore('theme', () => {
  const colorMode = useColorMode()
  const darkThemes = new Set(['dark','forest','black','dracula','night','cyberpunk','synthwave','retro','business','acid'])
  const lightThemes = new Set(['light', 'cupcake', 'bumblebee', 'emerald', 'corporate', 'valentine', 'halloween', 'garden', 'aqua', 'lofi', 'pastel', 'fantasy', 'wireframe', 'luxury', 'cmyk', 'autumn', 'coffee', 'lemonade', 'winter'])
  
  const themeCookieOptions = {
    maxAge: 60 * 60 * 24 * 30 * 6,
    sameSite: 'lax',
    secure: false,
    path: '/',
  }

  const theme = useCookie('theme', {
    ...themeCookieOptions,
    default: () => 'system',
  })

  const setTheme = (newTheme) => {
    theme.value = newTheme
    colorMode.preference = newTheme
    const root = document.documentElement
    root.setAttribute('data-theme', newTheme)
    root.classList.remove(...root.classList)
    root.classList.add(newTheme)
  }

  // Mount anında tema uygula
  if (theme.value !== colorMode.preference) {
    setTheme(theme.value)
  }

  return {
    theme,
    setTheme,
    darkThemes,
    lightThemes,
  }
})
