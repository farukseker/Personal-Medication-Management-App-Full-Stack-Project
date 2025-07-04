<template>
  <!-- <History.vue /> -->
   <div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takibi</h1>
            <button 
              @click="go('/settings')"
              class="btn btn-ghost text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>
      <div>
        <div class="flex w-full my-2">
          <h2 class="text-lg font-semibold w-full my-auto">
            <TodayMessage />
          </h2>
          <button class="btn btn-sm btn-success">Rapor Al </button>
        </div>
        <div class="card bg-base-100 sm:shadow mb-3">
            <div class="card-body flex flex-row gap-2 p-0 sm:p-5 w-full justify-between">
                <button class="btn btn-sm"
                :class="filter_type === 'today' ? 'btn-primary': 'btn-outline'"
                @click="filter_type='today'">Bugün</button>
                <button class="btn btn-sm"
                :class="filter_type === 'yesterday' ? 'btn-primary': 'btn-outline'"
                @click="filter_type='yesterday'">Dün</button>
                <button class="btn btn-sm"
                :class="filter_type === 'week' ? 'btn-primary': 'btn-outline'"
                @click="filter_type='week'">Bu hafta</button>
                <button
                class="btn btn-sm"
                :class="filter_type === 'month' ? 'btn-primary': 'btn-outline'"
                @click="filter_type='month'">Bu Ay</button>
                <button class="btn btn-sm btn-outline text-secondary">Özel Tarih </button>
            </div>
        </div>
        <div class="underline font-semibold text-primary-content" v-if="!(medication_history_list?.length > 0)">
          liste boş
        </div>
        <div class="space-y-3" v-if="filter_type === 'today' || filter_type === 'yesterday'">
          <MedicationPillReminder v-for="medication_today in medication_history_list" :key="medication_today.id + 3" :medication="medication_today" @load_medication='load_medication_history_list' />
        </div>
        <div class="space-y-3" v-else>
          <div class="flex">
            <span class="my-auto">Tarih sıralaması</span>
            <button @click="is_revresed_list=!is_revresed_list" class="btn btn-sm btn-ghost px-1" >
              <span>{{ is_revresed_list ? 'Yukarı':'Aşağı' }}</span>
            </button>
          </div>
          <div v-for="split_medication_history in split_medication_history_list">
            <div class="w-full flex gap-2">
              <span class="min-w-fit my-auto">{{ get_readable_date(split_medication_history.date) }}</span>
              <hr class="w-full my-auto">
            </div>
            <div class="flex flex-col gap-2">
              <MedicationPillReminder
                v-for="medication_today in split_medication_history.medication_logs"
                :key="medication_today.id + 3"
                :medication="medication_today"
                @load_medication='load_medication_history_list'
              />
            </div>
          </div>
        </div>
      </div>
   </div>
</template>
  
<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
const { $api } = useNuxtApp()
import dayjs from 'dayjs'

const medication_history_list = ref([])
const split_medication_history_list = ref([])
const filter_type = ref('today') //today 

const is_revresed_list = ref(false) 

watch(filter_type, async new_filter_type => {
  if (new_filter_type === 'today' || new_filter_type === 'yesterday' ) {
    medication_history_list.value = await $api(`/medication/medication-logs/?date=${new_filter_type}`)
  } else {
      split_medication_history_list.value = await $api(`/medication/medication-logs/split/?date=${new_filter_type}&reverse=${is_revresed_list.value}`)
  }
})

watch(is_revresed_list, async is_revresed_list_new => {
  split_medication_history_list.value = await $api(`/medication/medication-logs/split/?date=${filter_type.value}&reverse=${is_revresed_list_new}`)
})


const load_medication_history_list = async () => medication_history_list.value = await $api('/medication/medication-logs/?date=today')
onMounted(load_medication_history_list)

const get_readable_date = (date) => {
  return dayjs(date).locale('tr').format('DD MMMM YYYY')
}

//'/medication/medication-logs/23/'
</script>
