<template>
<label class="relative w-full inline-block">
  <font-awesome v-if="darkThemes.has(themeStore.theme)" :icon="faMoon" class="absolute left-5 top-1/2 -translate-y-1/2 pointer-events-none z-10" />
  <font-awesome v-else-if="lightThemes.has(themeStore.theme)" :icon="faSun" class="absolute left-5 top-1/2 -translate-y-1/2 pointer-events-none z-10" />
  <font-awesome v-else :icon="currentIcon" class="absolute left-5 top-1/2 -translate-y-1/2 pointer-events-none z-10" />
  <select 
    class="select w-full pl-10 font-semibold"
    v-model="selectedTheme"
  >
    <option disabled selected>Theme</option>
    <option v-for="theme of themes" :key="theme">{{ theme }}</option>
  </select>
</label>
</template>

<script setup>
import { 
    faSun,
    faMoon,
    faCircleHalfStroke
} from '@fortawesome/free-solid-svg-icons'
const themes = [
  'system',
  'light',
  'dark',
  'cupcake',
  'bumblebee',
  'emerald',
  'corporate',
  'synthwave',
  'retro',
  'cyberpunk',
  'valentine',
  'halloween',
  'garden',
  'forest',
  'aqua',
  'lofi',
  'pastel',
  'fantasy',
  'wireframe',
  'black',
  'luxury',
  'dracula',
  'cmyk',
  'autumn',
  'business',
  'acid',
  'lemonade',
  'night',
  'coffee',
  'winter',
]

const themeStore = useThemeStore()

onMounted(() => {
  themeStore.setTheme(themeStore.theme)
})


const selectedTheme = computed({
  get: () => themeStore.theme,
  set: val => themeStore.setTheme(val),
})


const darkThemes = new Set([
  'dark',
  'forest',
  'black',
  'dracula',
  'night',
  'cyberpunk',
  'synthwave',
  'retro',
  'business',
  'acid',
])

const lightThemes = new Set([
  'light',
  'cupcake',
  'bumblebee',
  'emerald',
  'corporate',
  'valentine',
  'halloween',
  'garden',
  'aqua',
  'lofi',
  'pastel',
  'fantasy',
  'wireframe',
  'luxury',
  'cmyk',
  'autumn',
  'coffee',
  'lemonade',
  'winter',
])
/*

const theme = ref('light')

onMounted(async () => {
  theme.value = localStorage.getItem('theme') || 'light'
  applyTheme(theme.value)
})

function applyTheme(newTheme) {
  document.documentElement.setAttribute('class', newTheme)
  document.documentElement.setAttribute('data-theme', newTheme)
  localStorage.setItem('theme', newTheme)
  if (colorMode) colorMode.preference = newTheme
}

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
  applyTheme(theme.value)
}

watch(theme, (newTheme) => {
  applyTheme(newTheme)
})
*/

const currentIcon = computed(() => {
  if (darkThemes.has(themeStore.theme.value)) return faMoon
  if (lightThemes.has(themeStore.theme.value)) return faSun
  return faCircleHalfStroke // system vs için
})
</script>