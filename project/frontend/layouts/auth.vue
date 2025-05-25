<template>

<div class="font-[Roboto] w-full">
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