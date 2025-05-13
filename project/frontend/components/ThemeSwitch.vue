<template>
    <label class="swap swap-rotate cursor-pointer text-2xl">
        <input type="checkbox" :checked="theme === 'dark'" @change="toggleTheme" />

        <!-- Gündüz ikon -->
        <svg class="swap-on fill-current w-6 h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M5.64 17.657A9 9 0 0012 21a9 9 0 100-18 9 9 0 00-6.36 15.657z" />
        </svg>

        <!-- Gece ikon -->
        <svg class="swap-off fill-current w-6 h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M21.64 13.657A9 9 0 1110.343 2.36 7 7 0 0021.64 13.657z" />
        </svg>
    </label>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const theme = ref('light')

// onMounted(() => {
//     document.documentElement.setAttribute('data-theme', theme.value)
// })

function toggleTheme() {
    theme.value = localStorage.getItem('theme') || 'light'
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
    document.documentElement.setAttribute('class', theme.value)
    document.documentElement.setAttribute('data-theme', theme.value)
    localStorage.setItem('theme', theme.value)
}
</script>