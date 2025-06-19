<template>
    <div class="p-4 space-y-4 max-w-md mx-auto flex flex-col">
      <div class="flex flex-col gap-4 flex-1 max-h-fit">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">Ayarlar</h1>
            <button 
            @click="go('/')"
            class="btn btn-ghost text-2xl p-0">
              <font-awesome :icon="faArrowLeft" />
            </button>
            </div>
        </div>
      <div>

    <section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4 gap-4">
      <legend class="fieldset-legend font-bold">Kullanıcı</legend>
      <div class="flex gap-4">
        <div class="min-w-[46px] min-h-[46px] max-w-[46px] max-h-[46px] bg-gray-600 rounded-full relative cursor-pointer">
          <font-awesome :icon="faImage" class="absolute -top-1 -left-2 p-1 bg-white rounded-full shadow border scale-75 text-gray-700" />
          <img class="w-full h-full object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
        </div>
        <div v-if="user_info" class="my-auto w-full">
          {{ user_info?.first_name }} {{ user_info?.last_name }}
          <br>
          {{ user_info?.email }}
        </div>
      </div>
    </fieldset>
    
    <fieldset v-if="user_info" class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4 gap-4">
        <legend class="fieldset-legend font-bold">Kullanıcı bilgileri</legend>
        <div class="flex gap-2">
          <div>
            <label>Adınız</label>
            <input v-model="user_info.first_name" class="input w-full" type="text" placeholder="Ad">
          </div>
            <div>
            <label>Soy Adınız</label>
            <input v-model="user_info.last_name" class="input w-full" type="text" placeholder="Soy Ad">
          </div>
        </div>
        <div>
          <label>E-Mail</label>
          <input v-model="user_info.email" class="input w-full" type="email" placeholder="Email">
        </div>
    </fieldset>
    
    <form>
        <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4 gap-4">
          <legend class="fieldset-legend font-bold">Şifre değiştir</legend>
          <label>
            <span>Eski Şifreniz</span>
            <font-awesome :icon="faCircle" class="scale-50 mx-1 text-gray-200" />
            <a>Şifrenizi mi unuttunuz ?</a></label>
          <input class="input w-full" type="password" autocomplete="password" placeholder="Şifreniz">
          <label>Yeni Şifreniz</label>
          <input class="input w-full" type="password" autocomplete="new-password" placeholder="Yeni Şifreniz">
          <div class="w-full flex">
            <div class="w-full"></div>
            <button class="btn btn-primary w-fit">Kaydet</button>
          </div>
      </fieldset>
    </form>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
      <legend class="fieldset-legend font-bold">Dil Ayarları</legend>
        <NuxtLink v-for="locale in availableLocales" :key="locale.code" :to="switchLocalePath(locale.code)">
          {{ locale.name }}
        </NuxtLink>
    </fieldset>

    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Tema Ayarları</legend>
        <button
          class="btn"
          :class="theme === 'light' ? 'btn-block': 'btn-outline'"
              @click="toggleTheme"
            >
              <span v-if="theme === 'light'">
                <font-awesome :icon="faSun" /> 
              </span>
              <span v-else>
                <font-awesome :icon="faMoon" /> 
              </span>
              {{ theme !== 'light' ? 'Karanlık' : 'Aydınlık' }}
            </button>
    </fieldset>

    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <button class="btn btn-error" @click="logout">
          <font-awesome :icon="faUser" />
          Çıkış yap
        </button>
      </fieldset>
    </section>
    </div>
    </div>
</template>

<script setup>
import { faUser, faMoon, faSun, faArrowLeft, faCircle, faHome, faImage } from '@fortawesome/free-solid-svg-icons'
const { $api } = useNuxtApp()
const { locale, locales } = useI18n()
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()

const switchLocalePath = useSwitchLocalePath()
const availableLocales = computed(() => {
  // return locales.value.filter(i => i.code !== locale.value)
  return locales.value
})

const user_info = ref(null)

const get_user_info = async () => user_info.value = await $api('/auth/info/')


const theme = ref('light')

onMounted(async () => {
  theme.value = localStorage.getItem('theme') || 'light'
  await get_user_info()
  // theme.value = theme.value === 'light' ? 'light' : 'dark'
})

function toggleTheme() {
    theme.value = localStorage.getItem('theme') || 'light'
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
    document.documentElement.setAttribute('class', theme.value)
    document.documentElement.setAttribute('data-theme', theme.value)
    localStorage.setItem('theme', theme.value)
}


const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')
const router = useRouter()

const logout = () => {
  accessToken.value = ''
  refreshToken.value = ''
  go('/auth/login')
}
</script>