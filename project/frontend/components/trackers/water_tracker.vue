<template>
  <div class="flex flex-col gap-4 items-center">
    <div class="flex w-full m-auto justify-center">
      <button class="btn btn-ghost">🎯 Yeni hedef belirle</button>
      <button class="btn btn-ghost">🔔 Hatırlatıcı ayarları</button>
    </div>

    <div class="space-y-4 py-4 grid grid-cols-2 gap-4">
      <div
        class="radial-progress text-blue-400 scale-150 text-xl"
        :style="`--value:${progress}`"
        :aria-valuenow="progress"
        role="progressbar"
      >
        <span class="text-lg">{{ total }} ml</span>
      </div>
      <div>
        <ul>
          <li><span class="font-semibold">Hedef</span>: {{ goal }} ml</li>
          <li><span class="font-semibold">Ulaşılan</span>: {{ total }} ml</li>
        </ul>
      </div>
    </div>

    <div class="grid grid-cols-2 gap-4 w-full">
      <div v-for="amount in [100, 250, 300, 400]" :key="amount" class="water-button" @click="() => addWater(amount)">
        <p class="my-auto flex flex-col mt-1">
          <font-awesome :icon="getIconFromAmount(amount)" class="my-auto text-lg" />
          <span class="text-lg font-bold text-center">{{ amount }} ml</span>
        </p>
      </div>
    </div>

    <div class="w-full flex flex-col gap-2 max-h-80 overflow-y-auto">
      <ul class="flex flex-col gap-2">
        <li
          v-for="entry in history"
          :key="entry.id"
          class="w-full bg-blue-50 dark:bg-blue-900 p-2 rounded grid grid-cols-6"
        >
          <div class="col-span-1 flex">
            <font-awesome :icon="getIconFromAmount(entry.amount)" class="m-auto text-xl" />
          </div>
          <div class="col-span-2 flex gap-2">
            <span class="my-auto">{{ entry.amount }}</span>
            <span class="my-auto text-sm">ml</span>
          </div>
          <div class="col-span-2 flex">
            <span class="my-auto">{{ formatTime(entry.timestamp) }}</span>
          </div>
          <button class="col-span-1 btn btn-sm btn-error" @click="deleteEntry(entry.id)">
            <font-awesome :icon="faX" />
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { faBucket, faGlassWater, faDroplet, faMugSaucer, faX } from '@fortawesome/free-solid-svg-icons'
const { $api } = useNuxtApp()

const goal = ref(0)
const history = ref([])
const total = computed(() => history.value.reduce((sum, h) => sum + h.amount, 0))
const progress = computed(() => Math.min(Math.round((total.value / goal.value) * 100), 100))

const formatTime = (timestamp) => {
  return new Date(timestamp).toLocaleTimeString('tr-TR', {
    hour: '2-digit',
    minute: '2-digit',
  })
}

const getIconFromAmount = (amount) => {
  switch (amount) {
    case 100: return faDroplet
    case 250: return faGlassWater
    case 300: return faMugSaucer
    case 400: return faBucket
    default: return faDroplet
  }
}

const fetchGoalAndEntries = async () => {
  try {
    const [goalResponse, entriesResponse] = await Promise.all([
      $api('/health/water/goal/'),
      $api('/health/water/entries/')
    ])
    goal.value = goalResponse.daily_goal
    history.value = entriesResponse.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
  } catch (error) {
    console.error('Veriler alınamadı:', error)
  }
}

const addWater = async (amount) => {
  try {
    const response = await $api('/health/water/entries/', {
      method: 'POST',
      body: { amount }
    })
    history.value.unshift(response)
  } catch (error) {
    console.error('Su eklenemedi:', error)
  }
}

const deleteEntry = async (id) => {
  try {
    await $api(`/health/water/entries/${id}/`, { method: 'DELETE' })
    history.value = history.value.filter((entry) => entry.id !== id)
  } catch (error) {
    console.error('Kayıt silinemedi:', error)
  }
}

onMounted(() => {
  fetchGoalAndEntries()
})
</script>

<style scoped>
.water-button {
  @apply btn btn-ghost flex p-4 min-h-16 max-h-16 flex-col justify-center border rounded-lg text-blue-800 bg-blue-200 shadow cursor-pointer;
}
</style>
