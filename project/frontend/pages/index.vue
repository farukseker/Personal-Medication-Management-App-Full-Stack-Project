<template>
  <!-- <İndex.vue /> -->
   <div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takibi</h1>
            <button 
              @click="$router.push('/settings')"
              class="btn btn-ghost text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>
      <div>
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, {{ today }}</h2>
          <button class="btn btn-primary btn-sm"
          @click="$router.push('/new_medicine/medicine_name')"
          >+ ilaç ekle</button>
        </div>
        <div class="space-y-3 max-h-[40vh] overflow-y-auto" >
          <MedicationPillReminder
          v-for="medication_today in medication_today_list"
          :key="medication_today.id" 
          :medication="medication_today" 
          @load_medication="async () => await load_medication_today_list()"

          />
        </div>
      </div>
      <!--div class="grid grid-cols-3 gap-4">
        <div class="rounded shadow-md bg-base-200 p-2 grid grid-cols-3 bg-fuchsia-800">
          <div class="col-span-2">Abdest</div>
          <div class="col-span-1">1</div>
        </div>
        <div class="rounded shadow bg-base-200 p-2">Count: 0</div>
        <div class="rounded shadow bg-base-200 p-2">Count: 0</div>
      </div-->
        <!-- Haftalık Durum -->
        <!--div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="text-md font-medium">Bu Gün</h3>
            <progress class="progress progress-primary w-full" value="60" max="100"></progress>
            <p class="text-sm text-gray-500 mt-1">6 / 10 doz alındı</p>
          </div>
        </div-->
   </div>
</template>
  
<script setup>
import { useMyMedicationStore } from '@/stores/my_medication_store.js'
import { NavNavigationShortcut } from '#components'
import { faTablets, faPills, faPlus, faGear, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'
import dayjs from 'dayjs'

// const my_medication_store = useMyMedicationStore()
// onMounted(my_medication_store.getMedicationList)
const { $api } = useNuxtApp()

const medication_today_list = ref([])
const today = ref()
const load_medication_today_list = async () => {
  const data = await $api('/medication/today/')
  medication_today_list.value = data
  return true // Burada önemli olan bir değer döndürmen
}
onMounted(load_medication_today_list)

onMounted(()=>{

    today.value = dayjs().format('mm. MMMM')
})

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
