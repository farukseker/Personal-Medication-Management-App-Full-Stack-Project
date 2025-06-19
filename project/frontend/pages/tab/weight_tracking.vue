<template>
  <div class="p-4 space-y-4 max-w-md mx-auto">
  <div class="flex flex-col gap-4 flex-1">
    <div class="flex justify-between items-center">
      <h1 class="text-xl font-bold">{{ $t('index.title') }}</h1>
      <button 
        @click="go('/settings')"
        class="btn btn-ghost btn-circle text-2xl p-0">
        <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
      </button>
    </div>
  </div>

  <div class="flex w-full">
    <h2 class="text-lg font-semibold mb-2 w-full">{{ $t('index.today') }}, {{ today }}</h2>
  </div>

  <NavTabsNav />

  <div class="w-full">
    <button 
      class="btn btn-primary w-full text-xl"
      @click="go('/tab/add_weight')"
    >Tartıl</button>
  </div>

  <section>
  <article>
    <TrackersWeightTracker />
  </article>
  </section>
</div>

</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
const route = useRoute()
const localePath = useLocalePath()
const scheduleStore = useNewMdcStore()
const isPathEqual = (path) => route.path === localePath(path) 

</script>
