<template>
<div class="flex flex-col gap-4 flex-1">
    <div class="flex justify-between items-center">
      <h1 class="text-xl font-bold">{{ title }}</h1>
      <button 
        @click="go('/settings')"
        class="btn btn-ghost btn-circle text-2xl p-0">
        <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
      </button>
    </div>
  </div>
  <div class="flex w-full my-2">
    <h2 class="text-lg font-semibold w-full">
      <TodayMessage />
    </h2>
    <slot />
  </div>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
defineProps({
    title: {
        Object: String,
        required: false,
        default: 'MediMind'
    }
})
</script>