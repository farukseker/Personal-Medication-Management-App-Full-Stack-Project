<template>
    <label class="label">Sıklık</label>
    <div class="join">
        <input 
            class="join-item btn btn-xs sm:btn-sm md:btn-md justify-start"
            type="checkbox"
            name="meal_status"
            v-model="medicineOftens"
            :value="often.value"
            :aria-label="often.label"
            v-for="(often, index) in often_list"
            :key="index"
            @click="add_time_to_reminder(often.time, $event.target.checked)"
          />
    </div>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'


const often_list = ref([
  {
    value: 'Morning',
    label: 'Sabah',
    time: '08:00'  
  },
  {
    value: 'Snack 1',
    label: 'Ara öğün',
    time: '10:00'  
  },
  {
    value: 'Lunch',
    label: 'Öğlen',
    time: '13:00'  
  },
  {
    value: 'Snack 2',
    label: 'Ara öğün',
    time: '15:00'  
  },
  {
    value: 'Evening',
    label: 'Akşam',
    time: '20:00'  
  },
])

const medicine_store = useMedicineFormStore()
const medicineOftens = computed({
  get: () => medicine_store.often_list,
  set: (val) => {
    medicine_store.often_list = val
  }
})

const add_time_to_reminder = (time, isChecked) => {
  isChecked ? medicine_store.addRemindTime(time) : ''
}
</script>