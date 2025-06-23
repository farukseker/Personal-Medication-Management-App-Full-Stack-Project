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
      <div 
          @click="go('/new_counter')"
          class="rounded shadow bg-base-200 border-2 border-dashed border-gray-400 text-gray-600 px-2 py-0 flex cursor-pointer min-w-fit text-sm">
          <span class="my-auto">{{ $t('counter.add_counter') }}</span>
      </div>
    </div>

  <NavTabsNav />

  <article>
    <fieldset class="w-full fieldset card rounded-box">
      <div class="grid grid-cols-3 gap-4">
        <CountersCounterList :counters_list="counters_list" />
        <CountersAddCounterLink />
      </div>
    </fieldset>
  </article>
</div>

</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { $api } = useNuxtApp()
const { go } = useLocaleRouter()

const counters_list = ref([])

const loadCounters = async () => {
    const data = await $api('/counter/')
    counters_list.value = data.map(counter => ({
      ...counter,
      is_progress: false
    }))
}

onMounted(() => {
  loadCounters()
})
</script>
