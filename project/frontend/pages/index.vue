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
      <div>
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, {{ today }}</h2>
          <button class="btn btn-primary btn-sm"
          @click="go_new_medicine_form"
          >+ ilaç ekle</button>
        </div>
        <div class="space-y-3 max-h-[40vh] overflow-y-auto mt-4" >
          <MedicationPillReminder
          v-if="medication_today_list.length > 0"
          v-for="medication_today in medication_today_list"
          :key="medication_today.id" 
          :medication="medication_today" 
          @load_medication="async () => await load_medication_today_list()"
          />
          <div v-else role="alert" class="alert alert-success shadow">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Bu gün almanız gereken ilaç bulunmamaktadır!</span>
          </div>
        </div>
      </div>
        <!-- Haftalık Durum -->
      <div class="card bg-base-100 shadow-md">
        <div class="card-body">
          <h3 class="text-md font-medium">Bu Gün</h3>
          <progress class="progress progress-primary w-full" :value="stats?.taken_percentage" max="100"></progress>
          <p class="text-sm text-gray-500 mt-1">{{ stats?.taken_count }} / {{ stats?.be_taken_count }} doz alındı</p>
        </div>
      </div>
  
      <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Sayaçlar</legend>
          <div class="grid grid-cols-3 gap-4">
            <div class="rounded shadow-md bg-base-200 p-2 grid grid-cols-3 bg-fuchsia-800">
              <div class="col-span-2">Abdest</div>
              <div class="col-span-1">1</div>
            </div>
            <div class="rounded shadow bg-base-200 p-2">Count: 0</div>
            <!-- Add a counter -->
            <div class="rounded shadow bg-base-200 border-2 border-dashed border-gray-400 text-gray-600 p-2 flex cursor-pointer">
              <span class="my-auto">Sayaç Ekle</span>
            </div>
          </div>
      </fieldset>
  
  </div>
</template>
  
<script setup>
import { faTablets, faPills, faPlus, faGear, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'
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
    const taken = h_r.length;
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
  await load_medication_today_list()
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
