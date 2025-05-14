<template>
  <!-- <FormsNewMedicationForm /> -->
   <div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takibi</h1>
            <button class="btn btn-ghost text-2xl">
              pp
            </button>
            </div>
        </div>
      <div>
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, 13 Mayıs</h2>
          <button class="btn btn-primary btn-sm">+ ilaç ekle</button>
        </div>
        <div class="space-y-3">
          <MedicationPillReminder v-for="medication_today in medication_today_list" :medication="medication_today" @load_medication='load_medication_today_list' />
        </div>
      </div>
        <!-- Haftalık Durum -->
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h3 class="text-md font-medium">Bu Gün</h3>
            <progress class="progress progress-primary w-full" value="60" max="100"></progress>
            <p class="text-sm text-gray-500 mt-1">6 / 10 doz alındı</p>
          </div>
        </div>
   </div>
</template>
  
<script setup>
import { useMyMedicationStore } from '@/stores/my_medication_store.js'
import { NavNavigationShortcut } from '#components'
import { faTablets, faPills, faPlus, faGear, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'

// const my_medication_store = useMyMedicationStore()
// onMounted(my_medication_store.getMedicationList)
const { $api } = useNuxtApp()

const medication_today_list = ref('')
const load_medication_today_list = async () => medication_today_list.value = await $api('/medication/today/')
onMounted(load_medication_today_list)

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
