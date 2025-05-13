<template>

<div class="font-[Roboto] w-full">
    <slot />
    <UNotifications />
    <div class="absolute bottom-10 right-2 z-10">
    <ThemeSwitch />
    </div>
</div>
</template>

<script setup>
onMounted(() => {
    const theme = localStorage.getItem('theme') || 'light'
    document.documentElement.setAttribute('data-theme', theme)
})
</script>