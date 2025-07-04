
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

  <div class="flex w-full my-2">
    <h2 class="text-lg font-semibold w-full">
      <TodayMessage />
    </h2>
    <button class="btn btn-primary btn-sm" @click="go_new_medicine_form">
      + {{ $t('index.add_medication') }}
    </button>
  </div>

  <NavTabsNav />

  <section>
    <article
      class="btn btn-ghost shadow text-warning font-semibold p-2"
      @click="handleSubscribe"
      v-if="!isUserAllowNotfication"
    >
        <font-awesome :icon="faWarning" />  
        Bİldirim alabilmek için, <span class="font-bold underline">izin vermelisiniz</span>
    </article>

    <div v-if="on_loading" class="w-full text-center">
      <span class="loading loading-infinity loading-md"></span>
    </div>
    <div v-else class="space-y-3 max-h-[40vh] overflow-y-auto py-4">
      <MedicationPillReminder
        v-if="medication_today_list.length > 0"
        v-for="medication_today in medication_today_list"
        :key="medication_today.id" 
        :medication="medication_today" 
        @load_medication="async () => await load_medication_today_list()" 
        class="mx-0.5"
        />
      <AlertsTakedAllPills v-else-if="stats?.taken_percentage == 100" />
      <AlertsPillsNotfound v-else />
    </div>
    <StatusWeeklyStatus v-if="stats" :stats="stats" />
  </section>
</div>
</template>
  
<script setup>
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
const route = useRoute()
const localePath = useLocalePath()
const scheduleStore = useNewMdcStore()
const isPathEqual = (path) => route.path === localePath(path) 

const isUserAllowNotfication = ref(false)
onMounted(async () => isUserAllowNotfication.value = Notification.permission === 'granted')

// const my_medication_store = useMyMedicationStore()
// onMounted(my_medication_store.getMedicationList)
const { $api } = useNuxtApp()
const medication_today_list = ref([])

const stats = ref()
const on_loading = ref(false)

const load_medication_today_list = async () => {
  const data = await $api('/medication/today/')
  medication_today_list.value = data
  await get_stats()
  return true 
}

const get_stats = async () => {
  if (medication_today_list.value){
    const h_r = await $api(`/medication/medication-logs/?date=today`)
    const taken = h_r.filter(e => e.taken_status === 'taken').length;
    const total = medication_today_list.value.length + taken;

    const percentage = total === 0 ? 0 : (taken / total) * 100;

    stats.value = {
      taken_count: taken,
      be_taken_count: total,
      taken_percentage: percentage.toFixed(2)
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
  go('/new_medicine/medicine_name')
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
