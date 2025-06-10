<template>
 <div class="min-h-screen bg-base-200 p-4 flex flex-col items-center">
    <h1 class="text-3xl font-bold text-primary mb-4">Kilo Takibi</h1>

    <div class="w-full max-w-xs bg-white shadow rounded-xl p-4 mb-4 text-center">
      <p class="text-lg font-semibold">Son Kilo:</p>
      <p class="text-3xl text-primary">
        {{ latestWeight }} kg
      </p>
      <p v-if="weightHistory.length > 1" class="mt-2 text-sm text-gray-500">
        Değişim: 
        <span :class="weightChange >= 0 ? 'text-red-500' : 'text-green-500'">
          {{ weightChange >= 0 ? '+' : '' }}{{ weightChange }} kg
        </span>
      </p>
    </div>

    <input
      v-model.number="newWeight"
      type="number"
      step="0.1"
      placeholder="Kilonu gir (kg)"
      class="input input-bordered input-primary w-full max-w-xs mb-4"
    />

    <button @click="addWeight" class="btn btn-primary w-full max-w-xs mb-4">
      Ekle
    </button>

    <ul class="w-full max-w-xs space-y-2">
      <li
        v-for="(entry, index) in weightHistory"
        :key="index"
        class="bg-white rounded-lg shadow p-3 text-sm flex justify-between"
      >
        <span>{{ entry.weight }} kg</span>
        <span class="text-gray-500">{{ entry.date }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>

const newWeight = ref(null)
const weightHistory = ref([])

const addWeight = () => {
  if (!newWeight.value || newWeight.value <= 0) return

  const now = new Date()
  weightHistory.value.unshift({
    weight: newWeight.value,
    date: now.toLocaleDateString('tr-TR'),
  })

  newWeight.value = null
}

const latestWeight = computed(() => {
  return weightHistory.value[0]?.weight || '-'
})

const weightChange = computed(() => {
  if (weightHistory.value.length < 2) return 0
  return (weightHistory.value[0].weight - weightHistory.value[1].weight).toFixed(1)
})

</script>