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
  <div class="w-full text-center">
    <font-awesome :icon="faWeightScale" class="text-4xl text-primary mx-2" />
    <div class="flex flex-col">
      <span class="text-lg border-b border-gray-400 max-w-fit mx-auto">Son kilo: {{ latestWeight }} kg</span>
      <span class="text-sm text-gray-500">Son değişim: {{ weightChange }} kg</span>
    </div>
  </div>
  <button 
    class="btn btn-primary w-full text-xl"
    @click="go('/tab/add_weight')"
  >
    Tartıl
  </button>
  <section>
    <article>
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
      </div>
    </article>
    <article>
        <div class="flex gap-2 w-full my-2">
          <span>Geçmişi</span>
          <hr class="w-full my-auto text-gray-400">
        </div>
        <ul class="w-full space-y-2 mb-6">
          <li
            v-for="(entry, index) in store.entries"
            :key="index"
            class="bg-base-100 dark:bg-base-200 rounded-lg shadow p-3 text-sm flex justify-between"
          >
            <p class="w-full my-auto">
              <font-awesome :icon="faWeightScale" class="text-secondary mx-2" />
              <span class="text-gray-500 min-w-fit">{{ entry.date }}</span>
              <font-awesome :icon="faCircle" class="scale-60 text-secondary mx-2" />
              <span class="text-start w-full">{{ entry.weight }} kg</span>
            </p>
            <button
              class="btn btn-sm btn-error"
              @click="store.deleteEntry(entry.id)"  
            >sil</button>
          </li>
        </ul>
    </article>
  </section>
</div>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
import { faCircle, faWeightScale } from '@fortawesome/free-solid-svg-icons'

const { go } = useLocaleRouter()
const route = useRoute()
const localePath = useLocalePath()
const isPathEqual = (path) => route.path === localePath(path) 

const store = useWeightEntryStore()

onMounted(() => store.fetchEntries())

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
