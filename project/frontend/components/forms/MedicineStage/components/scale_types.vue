<template>
    <label class="label">Ölçek</label>
    <div class="join">
        <input class="join-item btn btn-sm md:btn-md" type="radio" name="scale_type" v-model="medicineScaleType" value="scale" aria-label="Ölçek" />
        <input class="join-item btn btn-sm md:btn-md" type="radio" name="scale_type" v-model="medicineScaleType" value="special" aria-label="Özel" />
    </div>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'


const medicine_store = useMedicineFormStore()
const medicineScaleType = computed({
  get: () => medicine_store.scale_type,
  set: (val) => {
    medicine_store.scale_type = val
  }
})
</script>