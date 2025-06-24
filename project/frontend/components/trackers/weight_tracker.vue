<template>
  <div class="flex flex-col items-center gap-4">

    <div class="w-full max-w-xl bg-base-100 dark:bg-base-300 rounded-xl shadow p-2">
      <h2 class="text-lg font-semibold text-center mb-2">Kilo Değişimi Grafiği</h2>
      <ApexChart
        type="line"
        height="300"
        :options="chartOptions"
        :series="chartSeries"
      />
    </div>

    <ul class="w-full space-y-2 mb-6">
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
const store = useWeightEntryStore()

const newWeight = ref(null)

onMounted(() => store.fetchEntries())

const addWeight = () => {
  store.addEntry(newWeight.value)
  newWeight.value = null
}

const latestWeight = computed(() => store.latestWeight)
const weightChange = computed(() => store.weightChange)

const chartSeries = computed(() => store.chartSeries)
const chartOptions = computed(() => ({
  chart: { id: 'weight-chart', toolbar: { show: false } },
  xaxis: { categories: store.chartCategories },
  stroke: { curve: 'smooth' },
  markers: { size: 4 },
  colors: ['#3b82f6'],
  yaxis: { title: { text: 'Kilo (kg)' } },
}))
</script>
