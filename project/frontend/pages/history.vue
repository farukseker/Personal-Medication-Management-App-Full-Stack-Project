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
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, 13 Mayıs. Aldığın ilaçlar</h2>
        </div>
        <div class="card bg-base-100 shadow-md">
            <div class="card-boday flex flex-row gap-2 w-full">
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
                <button class="btn btn-sm btn-success">Rapor Al </button>
            </div>
        </div>
        <div class="space-y-3">
          <MedicationPillReminder v-for="medication_today in medication_history_list" :medication="medication_today" @load_medication='load_medication_history_list' />
        </div>
      </div>
   </div>
</template>
  
<script setup>
import { faTablets, faPills, faPlus, faGear, faCalendar, faHome, faUserGroup } from '@fortawesome/free-solid-svg-icons'
const { $api } = useNuxtApp()

const filter_type = ref('today')
watch(filter_type, async new_filter_type => {
    medication_history_list.value = await $api(`/medication/medication-logs/?date=${new_filter_type}`)
})

const medication_history_list = ref('')
const load_medication_history_list = async () => medication_history_list.value = await $api('/medication/medication-logs/?date=today')
onMounted(load_medication_history_list)
//'/medication/medication-logs/23/'
</script>
