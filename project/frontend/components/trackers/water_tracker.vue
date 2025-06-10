<template>
<div class="min-h-screen bg-blue-100 p-4 flex flex-col items-center">
    <h1 class="text-3xl font-bold text-blue-800 mb-4">Su Takibi</h1>

    <div class="radial-progress text-blue-600 mb-4" :style="{ '--value': progress }" role="progressbar">
      {{ total }} / {{ goal }} ml
    </div>

    <input
      v-model.number="input"
      type="number"
      placeholder="Ne kadar su içtin? (ml)"
      class="input input-bordered input-info w-full max-w-xs mb-4"
    />

    <button @click="addWater" class="btn btn-primary w-full max-w-xs mb-4">
      Ekle
    </button>

    <ul class="w-full max-w-xs space-y-2">
      <li
        v-for="(entry, index) in history"
        :key="index"
        class="bg-white rounded-lg shadow p-2 text-sm flex justify-between"
      >
        <span>{{ entry.amount }} ml</span>
        <span class="text-gray-500">{{ entry.time }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
// ------ su 
const goal = 2000 // Günlük hedef (ml)
const total = ref(0)
const input = ref(null)
const history = ref([])

const addWater = () => {
  if (!input.value || input.value <= 0) return

  total.value += input.value
  history.value.unshift({
    amount: input.value,
    time: new Date().toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' }),
  })
  input.value = null
}

const progress = computed(() => Math.min(Math.round((total.value / goal) * 100), 100))
import { usePushNotification } from '~/composables/usePushNotification';

const { subscribe } = usePushNotification();

const handleSubscribe = () => {
  subscribe();
};

</script>