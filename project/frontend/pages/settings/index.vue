<template>
<section class="px-4 space-y-4 max-w-md mx-auto">
    <header>
        <button class="btn btn-ghost ps-0 text-xl">
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold">Ayarlar</h1>
    </header>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold">Kullanıcı ayarları</legend>
            <SettingsButton :icon="faUser" title="Kişisel bilgiler" to="/" />
            <SettingsButton :icon="faKey" title="Şifre değiştir" to="/settings/change_password" />
        </fieldset>
    </article>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold">Erişebilirlik ayarları</legend>
            <SettingsButton 
                :icon="faLanguage"
                title="Dil"
                to="/settings/change_language" 
                :description="locale.toUpperCase()"
            />
            <SettingsButton
                :icon="theme === 'light' ? faSun:faMoon"
                title="Tema"
                @click="toggleTheme"
                :description="theme"
                :showEndArrow="false"
            />
        </fieldset>
    </article>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold">Destek ve Hakkında</legend>
            <SettingsButton :icon="faHeadset" title="Destek" to="/" />
            <SettingsButton :icon="faScroll" title="Hakkında" to="/" />
        </fieldset>
    </article>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <SettingsButton @click="logout" btnStyle="btn btn-ghost text-error" :icon="faDoorOpen" title="Çıkış yap" />
        </fieldset>
    </article>
    <p class="text-gray-400 text-sm text-center">Version. PARS | V1.12.8 - f4rukseker</p>
</section>
</template>

<script setup>
import { 
    faHeadset,
    faArrowLeft,
    faLanguage,
    faUser,
    faKey,
    faSun,
    faMoon,
    faDoorOpen,
    faScroll,
 } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
const { locale } = useI18n()
const theme = ref('light')

onMounted(async () => {
  theme.value = localStorage.getItem('theme') || 'light'
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

const logout = () => {
  accessToken.value = ''
  refreshToken.value = ''
  go('/auth/login')
}
</script>