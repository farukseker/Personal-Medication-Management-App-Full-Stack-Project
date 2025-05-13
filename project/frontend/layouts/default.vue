<template>
<UNotifications />
<div class="absolute bottom-10 right-2 z-10">
<ThemeSwitch />
</div>
<div class="font-[Roboto] flex flex-1 flex-col w-full">
    <div class="pb-20">
      <slot />
    </div>
    <div class="dock max-w-md mx-auto">
      <button>
        <font-awesome :icon="faHome" class="size-[1.2em]" />
        <span class="dock-label">Home</span>
      </button>
      
      <button class="">
        <font-awesome :icon="faPills" class="size-[1.2em]" />
        <span class="dock-label">İlaçlarım</span>
      </button>
        
      <button class="dock-active">
        <font-awesome :icon="faCalendar" class="size-[1.2em]" />
        <span class="dock-label">Geçmiş</span>
      </button>
      
      <button>
        <font-awesome :icon="faGear" />
        <span class="dock-label">Settings</span>
      </button>
    </div>
</div>
</template>

<script setup>
import { faTablets, faPills, faPlus, faGear, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'

onMounted(() => {
    const theme = localStorage.getItem('theme') || 'light'
    document.documentElement.setAttribute('data-theme', theme)
})

// useHead({
//   script: [
//     {
//       src: "https://analytics.farukseker.com.tr/script.js",
//       defer: true,
//       "data-website-id": "67e2e352-b6a5-448c-ba35-ddc4be704189"
//     }
//   ]
// })
</script>
