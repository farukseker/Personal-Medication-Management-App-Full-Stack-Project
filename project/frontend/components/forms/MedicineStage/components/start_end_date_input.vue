<template>
<div class="gap-2 w-full">
    <div>
        <label class="label">
            Başlangıç tarihi
        </label>
        <input type="date" class="input input-sm md:input-md w-full" v-model="medicineStartDate">
    </div>
    <div>
        <label class="label">
            Bitiş tarihi    
        </label>
        <input type="date" class="input input-sm md:input-md w-full" v-model="medicineEndDate">
    </div>
</div>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'
import dayjs from 'dayjs' // Tarih işlemleri için kullanışlı


const medicine_store = useMedicineFormStore()
const medicineStartDate = computed({
  get: () => medicine_store.start_date,
  set: (val) => {
    medicine_store.start_date = val
  }
})
const medicineEndDate = computed({
  get: () => medicine_store.end_date,
  set: (val) => {
    medicine_store.end_date = val
  }
})

onMounted(() => {
    const today = dayjs().format('YYYY-MM-DD')
    const nextWeek = dayjs().add(7, 'day').format('YYYY-MM-DD')
    medicine_store.start_date = today
    medicine_store.end_date = nextWeek
})
</script>