<template>
<div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaçlarım</h1>
            <button 
              @click="go('/settings')"
              class="btn btn-ghost text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>
      <div>
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full"><TodayMessage /></h2>
          <button 
          class="btn btn-primary btn-sm"
          @click="go_new_medicine_form"
          >+ ilaç ekle</button>
        </div>
        <div class="space-y-3 pt-2">
          <MedicationPillListItem
          v-for="medication in my_medication_list" 
          :key="medication.id + 'medication_lcl'" 
          :medication="medication"
          @do_plan_exist_medication="action_switch_to_plan"
          @update_exist_medication="action_switch_to_update"
          @load_medication_list="load_my_medication_list" 
          />
        </div>
      </div>
   </div>
</template>

<script setup>
const { $api } = useNuxtApp()
import dayjs from 'dayjs'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const today_month_name = ref(null)
const { go } = useLocaleRouter()

const scheduleStore = useNewMdcStore()
const my_medication_list = ref([])
const today = ref()

// const load_my_medication_list = async () => my_medication_list.value = await $api('/medication/medications/')
const load_my_medication_list = async () => my_medication_list.value = await $api('/medication/medications/')
onMounted(load_my_medication_list)
onMounted(()=>{
    today.value = dayjs().format('DD MMMM')
})

const go_new_medicine_form = () => {
  scheduleStore.resetForm()
  go('/new_medicine/medicine_name')
}

const action_switch_to_update = async (medication_id) => {
  const be_updated_medication = await $api(`/medication/medications/${medication_id}/`)
  scheduleStore.refull_self(be_updated_medication)
  go('/new_medicine/medicine_name')
}

const action_switch_to_plan = async (medication_id) => {
  const be_updated_medication = await $api(`/medication/medications/${medication_id}/`)
  scheduleStore.refull_self(be_updated_medication)
  go('/new_medicine/medicine_plan')
}
</script>