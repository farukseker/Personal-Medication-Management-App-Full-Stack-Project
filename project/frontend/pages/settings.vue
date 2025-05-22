<template>
    <div class="p-4 space-y-4 max-w-md mx-auto h-screen flex flex-col">
      <div class="flex flex-col gap-4 flex-1 max-h-fit">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">Ayarlar</h1>
            <button 
            @click="$router.push('/')"
            class="btn btn-ghost text-2xl p-0">
              <font-awesome :icon="faArrowLeft" />
            </button>
            </div>
        </div>
      <div>
    <ul class="menu bg-base-200 rounded-box w-full text-lg mx-auto">
  <li>
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
      </svg>
      Item 2 
    </a>
  </li>
  <li>
    <a
      @click="toggleTheme"
    >
      <span v-if="theme === 'light'">
        <font-awesome :icon="faSun" /> 
        
      </span>
      <span v-else>
        <font-awesome :icon="faMoon" /> 
        
      </span>
      {{ theme !== 'light' ? 'Karanlık' : 'Aydınlık' }}
    </a>
  </li>
  <li>
    <a
    class="text-red-400"
     @click="logout"
    >
      <font-awesome :icon="faUser" />
      Çıkış yap
    </a>
  </li>
</ul>
      </div>
      </div>
</template>

<script setup>
import { faUser, faMoon, faSun, faArrowLeft, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'


const theme = ref('light')

onMounted(() => {
  theme.value = localStorage.getItem('theme') || 'light'
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
  router.push('/auth/login')
}
</script>