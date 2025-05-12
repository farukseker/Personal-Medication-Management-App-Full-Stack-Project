<template>
    <section class="w-full flex flex-col gap-4 px-4 pt-2 font-mono">
        <fieldset class="w-full fieldset bg-gradient-to-b border-b-2 shadow-md from-base-300 to-base-100 border-base-300 rounded-box p-4">
        <legend class="fieldset-legend">İlaç seç</legend>
        <select v-model="selected_medicine" class="select w-full border">
            <option disabled value="">İlaç seç</option>
            <option
            :value="my_medication"
            v-for="(my_medication, index) in my_medication_store.myMedicationList"
            :key="index"
            >
            {{ my_medication.name }}
            </option>
        </select>
        <p class="label"></p>
    </fieldset>
    <fieldset v-if="filteredStages" class="w-full fieldset bg-gradient-to-b border-b-2 shadow-md from-base-300 to-base-100 border-base-300 rounded-box p-4">
        <legend class="fieldset-legend">Almanız gereken doz</legend>
        <div class="flex gap-2">
            <div class="flex flex-col text-center w-1/3 my-auto">
                <h2 class="text-primary text-4xl">
                    {{ filteredStages.unit }}
                </h2>
                <hr>
                <h3 class="text-secondary text-2xl">
                    {{ filteredStages.unit_type }}
                </h3>
            </div>
            <div class="w-full">
                <p>
                    <font-awesome :icon="faCalendar" /> <strong>Kullanım programı</strong> 
                    <br>
                    kullanmanız gereken doz: {{ filteredStages.unit }} {{ filteredStages.unit_type }}
                    <br>
                    başlangıç: {{ filteredStages.range_start_date }}
                    <br>
                    bitiş tarihi:  <span 
                    :class="is_stage_end ? '': 'text-red-600'"
                    >{{ filteredStages.range_end_date }}</span>
                    
                </p>
            </div>
        </div>
    </fieldset>  
    <fieldset v-if="filteredStages" class="w-full fieldset bg-gradient-to-b border-b-2 shadow-md from-base-300 to-base-100 border-base-300 rounded-box p-4">
        <legend class="fieldset-legend">Farklı doz kullanımı</legend>
        <input type="text" class="input w-full">
        <input type="text" class="input w-1/3">

    </fieldset>

</section>

</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useMyMedicationStore } from '@/stores/my_medication_store.js'
import { faPills, faCalendar } from '@fortawesome/free-solid-svg-icons'

const my_medication_store = useMyMedicationStore()

// const selected_medicine = ref(null)
const selected_medicine = ref({ "id": 3, "stages": [ { "id": 2, "unit": 2, "unit_type": "MG", "range_start_date": "2025-05-11", "range_end_date": "2025-05-15", "range_length": 1, "range_type": "week" }, { "id": 1, "unit": 13, "unit_type": "Tane", "range_start_date": "2025-05-11", "range_end_date": "2025-05-11", "range_length": 2, "range_type": "day" }, { "id": 3, "unit": 1, "unit_type": "miligram", "range_start_date": "2025-05-12", "range_end_date": "2025-05-26", "range_length": 1, "range_type": "end" } ], "often": [ "Morning", "Lunch", "Evening" ], "history": [], "name": "ADALAT CRONO 60 MG 20 KONT SAL TABLET", "notes": "", "hunger_situation": "hunger", "start_date": "2025-05-11", "end_date": "2025-05-26" })

onMounted(my_medication_store.getMyMedicationList)
onMounted(my_medication_store.getNextMedicationList)

// stages içinde bugünün tarihine denk geleni filtrele
import dayjs from 'dayjs'
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter'
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore'
const is_stage_end = ref(false)

dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)

const filteredStages = computed(() => {
  const medicine = selected_medicine.value
  if (!medicine || !medicine.stages) return null

  const stages = medicine.stages

  // tek elemanlıysa direkt dön
  if (stages.length === 1) {
    const stage = stages[0]
    const end = dayjs(stage.range_end_date)
    is_stage_end.value = today.isSameOrBefore(end)
    return stage
  }

  const today = dayjs()
  return stages.find(stage => {
    const start = dayjs(stage.range_start_date)
    const end = dayjs(stage.range_end_date)
    return today.isSameOrAfter(start) && today.isSameOrBefore(end)
  })
})
</script>
