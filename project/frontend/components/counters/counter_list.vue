<template>
<div
    v-for="(counter, index) in counters_list"
    :key="index" 
    @click="() => counter_tick(index)"
    class="rounded shadow-md bg-base-200 p-2 grid grid-cols-5 text-white"
    :class="counter.is_progress ? 'bg-fuchsia-700':'cursor-pointer bg-fuchsia-800'"
    >
    <div v-if="!counter.is_progress" class="col-span-2 full my-auto">{{ counter.name }}</div>
    <div v-if="!counter.is_progress" class="col-span-2 min-w-fit my-auto flex gap-2">{{ counter.count }} <p class="text-xs scale-90" v-if="counter.unit">{{ counter.unit }}</p></div>
    <div v-if="!counter.is_progress" class="col-span-1 text-center ">
        <font-awesome :icon="faPlus" />
    </div>
    <div v-else class="col-span-5 flex">
        <span class="loading loading-spinner loading-xs m-auto"></span>
    </div>
</div>
</template>

<script setup>
import { faPlus } from '@fortawesome/free-solid-svg-icons'
const { $api } = useNuxtApp()

const { counters_list } = defineProps({
    counters_list: {
        type: Array,
        required: true
    }
})

const counter_tick = async (counter_index) => {
  try {
    let counter_id = counters_list[counter_index].id
    counters_list[counter_index].is_progress = true
    await $api('/counter/tick/', {
      method: 'POST',
      body: {
        counter: counter_id,
        value: 1
      }
    })
    ++counters_list[counter_index].count
  } catch (e) {
    console.error(e)
  } finally {
    counters_list[counter_index].is_progress = false
  }
}

</script>