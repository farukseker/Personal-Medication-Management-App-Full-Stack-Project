<template>

<div class="font-[Roboto] px-4 space-y-4 max-w-md mx-auto">
    <slot />
    <UNotifications />
</div>
</template>

<script setup>
onMounted(() => {
    const theme = localStorage.getItem('theme') || 'light'
    document.documentElement.setAttribute('data-theme', theme)
})
</script>