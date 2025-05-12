<template>
    <div class="flex flex-col w-full">
        <label class="label" for="unit_range">
            Miktar
        </label>
        <input 
        id="unit_range"
        v-model="medicineIncreasingRange"
        :class="'input input-sm md:input-md border ' + (!(medicineIncreasingRange > 0) ? 'outline outline-red-500 focus:outline-red-500 active:outline-red-500':'')" min="1" 
        type="number" >
    </div>
    <div class="w-full">
        <label class="label block" for="unit_type">Ölçek</label>
        <select
        id="unit_type"
        :value="medicineWeightType" class="select select-sm md:select-md w-full">
            <option v-for="(measurement_unit, index) in measurement_units" :key="index" :value="measurement_unit.param">
                {{ measurement_unit.value }}
            </option>
        </select>
    </div>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'

defineProps({
    measurement_units: Array
})

const medicine_store = useMedicineFormStore()
const medicineIncreasingRange = computed({
  get: () => medicine_store.increasing_range,
  set: (val) => {
    medicine_store.increasing_range = val
  }
})

const medicineWeightType = computed({
  get: () => medicine_store.weight_type,
  set: (val) => {
    medicine_store.weight_type = val
  }
})

onMounted(() => {medicine_store.weight_type='miligram'; medicine_store.increasing_range = 1})
</script>