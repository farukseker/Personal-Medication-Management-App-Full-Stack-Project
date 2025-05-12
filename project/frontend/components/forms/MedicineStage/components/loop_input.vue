<template>
    <div class="flex flex-col w-full">
        <label class="label">
            Tekrar
        </label>
        <div class="w-full flex gap-2">
            <input class="input input-sm md:input-md w-full" min="1" v-model.number="medicineDirectionRange" type="number">
            <select v-model="medicineDirectionRangeType" class="select select-sm md:select-md w-full">
                <option value="day">Gün</option>
                <option value="week">Hafta</option>
                <option value="month">Ay</option>
                <option value="year">Yıl</option>
            </select>
        </div>
    </div>
</template>
<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'

const medicine_store = useMedicineFormStore()
const medicineDirectionRange = computed({
  get: () => medicine_store.direction_range,
  set: (val) => {
    medicine_store.direction_range = val
  }
})

const medicineDirectionRangeType = computed({
  get: () => medicine_store.direction_range_type,
  set: (val) => {
    medicine_store.direction_range_type = val
  }
})

onMounted(() => {medicine_store.direction_range = 1, medicine_store.direction_range_type='week'})
</script>