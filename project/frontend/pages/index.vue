<template>
  <!-- <İndex.vue /> -->
   <div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">{{ $t('index.title') }}</h1>
            <button 
              @click="$router.push('/settings')"
              class="btn btn-ghost btn-circle text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>

        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">{{ $t('index.today') }}, {{ today }}</h2>
          <button class="btn btn-primary btn-sm"
          @click="go_new_medicine_form"
          >+ {{ $t('index.add_medication') }}</button>
        </div>
    <button @click="handleSubscribe" class="px-4 py-2 bg-blue-600 text-white rounded">
      Bildirim Aboneliği Başlat
    </button>
      <div role="tablist" class="tabs tabs-lift tabs-md tabs-top">
        <a role="tab" @click="tab_index=0" class="tab hover:text-green-500 flex gap-2" :class="tab_index === 0 ? 'tab-active text-primary':''"><font-awesome :icon="faPills"/> {{ $t('index.medications') }}</a>
        <a role="tab" @click="tab_index=1" class="tab hover:text-green-500 flex gap-2" :class="tab_index === 1 ? 'tab-active text-primary':''"><font-awesome :icon="faPlus"/> {{ $t('index.counter') }}</a>
        <a role="tab" @click="tab_index=2" class="tab hover:text-green-500 flex gap-2" :class="tab_index === 2 ? 'tab-active text-primary':''"><font-awesome :icon="faGlassWater"/> {{ $t('index.water_tracking') }}</a>
        <a role="tab" @click="tab_index=3" class="tab hover:text-green-500 flex gap-2" :class="tab_index === 3 ? 'tab-active text-primary':''"><font-awesome :icon="faGlassWater"/> {{ $t('index.weight_tracking') }}</a>
      </div>
    
    <div v-if="on_loading" class="w-full flex">
      <span  class="loading loading-infinity loading-xl mx-auto"></span>
    </div>
    <section v-else>
      <article name="medication list" v-if="tab_index === 0">
        <div class="space-y-3 max-h-[40vh] overflow-y-auto py-4" >
          <MedicationPillReminder
            v-if="medication_today_list.length > 0"
            v-for="medication_today in medication_today_list"
            :key="medication_today.id" 
            :medication="medication_today" 
            @load_medication="async () => await load_medication_today_list()"
          />
          <AlertsTakedAllPills v-else-if="stats?.taken_percentage == 100" />
          <AlertsPillsNotfound v-else />
        </div>
        <StatusWeeklyStatus :stats="stats" />
      </article>
      <article name="counters view" v-if="tab_index === 1">
        <fieldset class="w-full fieldset card rounded-box ">
            <div class="grid grid-cols-3 gap-4">
              <CountersCounterList :counters_list="counters_list" />
              <CountersAddCounterLink />
            </div>
        </fieldset>
      </article>
      <article v-if="tab_index === 2">
        <TrackersWaterTracker />
      </article>
      <article v-if="tab_index === 3">
        <TrackersWeightTracker />
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
