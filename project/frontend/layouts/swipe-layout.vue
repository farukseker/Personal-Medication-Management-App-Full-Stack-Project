<template>
  <div
    v-touch:swipe.left="goNext"
    v-touch:swipe.right="goPrev"
    class="h-screen overflow-hidden"
  >
    <transition name="swipe" mode="out-in">
      <NuxtPage :key="route.fullPath" />
    </transition>
  </div>
</template>
<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const route = useRoute()
const { go } = useLocaleRouter()

// Lokal route tanımları (i18n'siz)
const rawPages = ['/', '/tab/counters', '/tab/water_tracking', '/tab/weight_tracking']

// Tam path’leri route’dan ayırmak için localePath wrapper kullanalım
const localePathPages = rawPages.map(path => useLocalePath()(path))

const currentIndex = computed(() =>
  localePathPages.indexOf(route.fullPath)
)

function isMobile() {
  return window.innerWidth <= 768
}

function goNext() {
  if (!isMobile()) return
  if (currentIndex.value < localePathPages.length - 1) {
    go(rawPages[currentIndex.value + 1])
  }
}

function goPrev() {
  if (!isMobile()) return
  if (currentIndex.value > 0) {
    go(rawPages[currentIndex.value - 1])
  }
}
</script>

<style scoped>
.swipe-enter-active,
.swipe-leave-active {
  transition: transform 0.3s ease;
  position: absolute;
  width: 100%;
}
.swipe-enter-from {
  transform: translateX(100%);
}
.swipe-leave-to {
  transform: translateX(-100%);
}
</style>