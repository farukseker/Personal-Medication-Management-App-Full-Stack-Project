<template>
<section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç plan</legend>
        
        <ScheduleList @edit="openEditModal" @remove="removeSchedule" />
        <button class="btn btn-primary mt-4" @click="$router.push('/new_medicine/medicine_plan_form')">+ Yeni Plan Ekle</button>

    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <div class="flex gap-2 w-full">
            <div class="w-full">
                <button class="btn btn-secondary w-full" @click="go_previous_page">Geri</button>
            </div>
            <div class="w-full">
                <button class="btn btn-primary w-full" @click="go_next_page">Devam et</button>
            </div>
        </div>
    </fieldset>
</section>
</template>

<script setup>
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
import { ref, reactive, computed } from 'vue'

const scheduleStore = useNewMdcStore()
const schedules = computed(() => scheduleStore.schedules)

const editIndex = ref(null)
const isModalVisible = ref(false)

const blankSchedule = () => ({
  start_date: '',
  end_date: '',
  frequency: 'daily',
  interval: 1,
  days_of_week: [],
  day_of_month: null,
  doses_per_period: 1,
  dose_amount: '',
  dose_unit: ''
})

const currentSchedule = reactive(blankSchedule())

function openNewModal() {
  Object.assign(currentSchedule, blankSchedule())
  editIndex.value = null
  isModalVisible.value = true
}

function openEditModal(index) {
  Object.assign(currentSchedule, JSON.parse(JSON.stringify(schedules.value[index])))
  editIndex.value = index
  isModalVisible.value = true
}

function saveSchedule(updatedSchedule) {
  if (scheduleStore.isOverlapping(updatedSchedule, editIndex.value)) {
    alert("Aynı tarihlerde başka bir plan zaten var. Lütfen tarihleri değiştir.")
    return
  }
  if (editIndex.value === null) {
    scheduleStore.addSchedule(updatedSchedule)
  } else {
    scheduleStore.updateSchedule(editIndex.value, updatedSchedule)
  }
  isModalVisible.value = false
}

function removeSchedule(index) {
  scheduleStore.removeSchedule(index)
}

const new_mdc_store = useNewMdcStore()
const router = useRouter()

const go_next_page = () => {
    new_mdc_store.form_index = 2
    router.push('/new_medicine/medicine_clock')
}
const go_previous_page = () => {
    new_mdc_store.form_index = 0
    router.push('/new_medicine/medicine_name')
}


definePageMeta({layout: 'newmdc'})
</script>