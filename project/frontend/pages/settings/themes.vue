<template>
    <section class="px-4 space-y-4 max-w-md mx-auto">
        <header>
            <button 
             class="btn btn-ghost ps-0 text-xl"
             @click="go('/settings')"
             >
                <font-awesome :icon="faArrowLeft" />
            </button>
            <h1 class="text-xl font-bold">Tema ayarları</h1>
        </header>
        <article>
            <fieldset class="w-full fieldset shadow rounded-box p-2">
                <legend class="fieldset-legend font-bold">Tema Seçiniz</legend>
                <label class="input w-full">
                    <font-awesome :icon="faSearch" />
                    <input type="text" class="grow" v-model="themeSearch" placeholder="Tema ara...">
                </label>
                <div class="flex">
                    <h2 class="min-w-fit">Renkörlüğü için</h2>
                    <hr class="w-full text-gray-300 my-auto ms-2">
                </div>
                <ColorPreview 
                @click="selectedTheme = 'colorblind'"
                theme="colorblind" 
                />

                <div class="flex">
                    <h2 class="min-w-fit">Tüm temalar</h2>
                    <hr class="w-full text-gray-300 my-auto ms-2">
                </div>
                <ul class="gap-2 grid grid-cols-2 md:grid-cols-3 flex-col mt-2">
                    <li 
                        v-for="theme of filteredThemes" :key="theme"
                        @click="selectedTheme = theme"
                        class="w-full rounded flex">
                        <ColorPreview :theme="theme" />
                    </li>
                </ul>
            </fieldset>
        </article>
    </section>
</template>
<script setup>
import { useLocaleRouter } from '#imports'
import { faArrowLeft, faSearch, faSun, faMoon, faCircleHalfStroke } from '@fortawesome/free-solid-svg-icons'
import { computed } from 'vue'

const { go } = useLocaleRouter()

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
  'colorblind'
]

const themeSearch = ref('')
const filteredThemes = computed(() => {
  return themes.filter(theme => 
    theme.toLowerCase().includes(themeSearch.value.toLowerCase())
  )
})


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
</script>