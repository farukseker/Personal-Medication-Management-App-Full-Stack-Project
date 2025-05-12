<template>
    <div class="flex gap-2">
        <div class="w-full">
            <label class="label block">Not<span class="text-gray-500">(opsiyonel)</span></label>
            <input 
                v-model="medicineNote"
                type="text" class="input input-sm md:input-md" placeholder="Notlar" />
        </div>
        <div class="w-1/6 md:w-1/4 flex flex-col">
            <label class="label opacity-0">Voice</label>
            <button class="btn btn-sm md:btn-md text-lg md:text-2xl">
                <font-awesome :icon="faMicrophone" />
            </button>
        </div>
    </div>
</template>

<script setup>
import { faMicrophone } from '@fortawesome/free-solid-svg-icons';
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'


const medicine_store = useMedicineFormStore()
const medicineNote = computed({
  get: () => medicine_store.medicine_notes,
  set: (val) => {
    medicine_store.medicine_notes = val
  }
})
</script>