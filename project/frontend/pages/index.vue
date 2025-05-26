<template>
  <!-- <İndex.vue /> -->
   <div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takibi</h1>
            <button 
              @click="$router.push('/settings')"
              class="btn btn-ghost btn-circle text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>

        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, {{ today }}</h2>
          <button class="btn btn-primary btn-sm"
          @click="go_new_medicine_form"
          >+ ilaç ekle</button>
        </div>
        
      <div role="tablist" class="tabs tabs-lift  tabs-lg">
        <a role="tab" @click="tab_index=0" class="tab flex gap-2" :class="tab_index === 0 ? 'tab-active text-primary':''"><font-awesome :icon="faPills"/> İlaçlar</a>
        <a role="tab" @click="tab_index=1" class="tab flex gap-2" :class="tab_index === 1 ? 'tab-active text-primary':''"><font-awesome :icon="faPlus"/> Sayaçlar</a>
        <a role="tab" @click="tab_index=2" class="tab flex gap-2" :class="tab_index === 2 ? 'tab-active text-primary':''"><font-awesome :icon="faGlassWater"/> Su Tüketimi</a>
      </div>
    
    <div v-if="on_loading" class="w-full flex">
      <span  class="loading loading-infinity loading-xl mx-auto"></span>
    </div>
    <section v-else>
      <article name="medication list" v-if="tab_index === 0">
        <div class="space-y-3 max-h-[40vh] overflow-y-auto mt-4" >

          <MedicationPillReminder
          v-if="medication_today_list.length > 0"
          v-for="medication_today in medication_today_list"
          :key="medication_today.id" 
          :medication="medication_today" 
          @load_medication="async () => await load_medication_today_list()"
          />
        
          <div v-else-if="stats?.taken_percentage == 100" role="alert" class="alert alert-success shadow text-white my-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Bu gün almanız gereken tüm ilaçları Aldınız!</span>
          </div>
        
          <div v-else role="alert" class="alert alert-info shadow my-2 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Bu gün almanız gereken ilaç bulunmamaktadır!</span>
          </div>

        </div>
        <!-- Haftalık Durum -->
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="text-md font-medium">Bu Gün</h3>
            <progress class="progress progress-primary rounded-e-none  w-full" :value="stats?.taken_percentage" max="100"></progress>
            <p class="text-sm text-gray-500 mt-1">{{ stats?.taken_count }} / {{ stats?.be_taken_count }} doz alındı</p>
          </div>
        </div>
      </article>
      <article name="counters view" v-if="tab_index === 1">
        <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
          <legend class="fieldset-legend font-bold">Sayaçlar</legend>
            <div class="grid grid-cols-3 gap-4">
              <div
                v-for="(counter, index) in counters_list"
                :key="index" 
                @click="() => counter_tick(index)"
                class="rounded shadow-md bg-base-200 p-2 grid grid-cols-5 text-white"
                :class="counter.is_progress ? 'bg-fuchsia-400':'cursor-pointer bg-fuchsia-800'"
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
              <!-- Add a counter -->
              <div 
              @click="$router.push('/new_counter')"
              class="rounded shadow bg-base-200 border-2 border-dashed border-gray-400 text-gray-600 p-2 flex cursor-pointer">
                <span class="my-auto">Sayaç Ekle</span>
              </div>
            </div>
        </fieldset>
      </article>
      <article v-if="tab_index === 2">
        eklenicek
      </article>
    </section>
  </div>
</template>
  
<script setup>
import { faPills, faPlus, faGlassWater } from '@fortawesome/free-solid-svg-icons'
import dayjs from 'dayjs'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const scheduleStore = useNewMdcStore()

// const my_medication_store = useMyMedicationStore()
// onMounted(my_medication_store.getMedicationList)
const { $api } = useNuxtApp()
const router = useRouter()
const medication_today_list = ref([])
const today = ref()
const stats = ref()
const on_loading = ref(false)
const tab_index = ref(0)

const counters_list = ref([])
watch (tab_index, async new_tab_index => {
  try {
    on_loading.value = true
    if (new_tab_index === 0){
      await load_medication_today_list()
    }
    if (new_tab_index === 1){
      await get_counters_list()
    }
  } catch (e) {
    console.error(e)
  } finally {
    on_loading.value = false
  }
})

const get_counters_list = async () => {
    const data = await $api('/counter/')
    counters_list.value = data.map(counter => ({
      ...counter,
      is_progress: false
    }))
}

const counter_tick = async (counter_index) => {
  try {
    let counter_id = counters_list.value[counter_index].id
    counters_list.value[counter_index].is_progress = true
    await $api('/counter/tick/', {
      method: 'POST',
      body: {
        counter: counter_id,
        value: 1
      }
    })
    ++counters_list.value[counter_index].count

  } catch (e) {
    console.error(e)
  } finally {
    counters_list.value[counter_index].is_progress = false
  }

  /*
  counter_id = 1
  response = client.post(f'/counter/tick/', json={
      "counter": counter_id,
      "unit": "Kez",
      "name": "İhtiyaç",
      "value": -1 # terse >
  })
  */
}

const load_medication_today_list = async () => {
  const data = await $api('/medication/today/')
  medication_today_list.value = data
  await get_stats()
  return true // Burada önemli olan bir değer döndürmen
}

onMounted(()=>{
    today.value = dayjs().format('DD MMMM')
})

const get_stats = async () => {
  if (medication_today_list.value){
    const h_r = await $api(`/medication/medication-logs/?date=today`)
    const taken = h_r.filter(e => e.taken_status === 'taken').length;
    const total = medication_today_list.value.length + taken;

    const percentage = total === 0 ? 0 : (taken / total) * 100;

    stats.value = {
      taken_count: taken,
      be_taken_count: total,
      taken_percentage: percentage.toFixed(2)  // virgülden sonra 2 basamak tutar
    };
  }
}

onMounted(async () => {
  try {
    on_loading.value = true
    await load_medication_today_list()
  } catch {} finally {
    on_loading.value = false
  }
})

const go_new_medicine_form = () => {
  scheduleStore.resetForm()
  router.push('/new_medicine/medicine_name')
}

useSeoMeta({
      title: 'İlaç Takip',
      ogTitle: 'İlaç Takip',
      description: 'İlaçlarını takip et sağlık durumunu kolayca raporla',
      ogDescription: 'İlaçlarını takip et sağlık durumunu kolayca raporla',
      ogImage: 'https://res.cloudinary.com/dlusw5ukg/image/upload/v1738064760/portfolyo/static/img/faruk2_buutol.jpg',
      twitterCard: 'summary_large_image',
      author: 'F4ruk-Seker'
})
</script>
