<template>
<UNotifications />
<div class="absolute bottom-10 right-2 z-10">
<ThemeSwitch />
</div>
<div class="font-[Roboto] flex flex-1 flex-col w-full">
    <div class="pb-20">
      <slot />
    </div>
    <NavBottomNav />
</div>
</template>

<script setup>

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
