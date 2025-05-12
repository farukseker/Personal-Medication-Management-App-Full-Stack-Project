<template>
    <label class="label">Açlık</label>
    <div class="join">
        <input class="join-item btn btn-sm md:btn-md" type="radio" name="hunger_situation" v-model="medicineHungerStation" value="non" aria-label="Fark etmez" />
        <input class="join-item btn btn-sm md:btn-md" type="radio" name="hunger_situation" v-model="medicineHungerStation" value="hunger" aria-label="Aç" />
        <input class="join-item btn btn-sm md:btn-md" type="radio" name="hunger_situation" v-model="medicineHungerStation" value="full" aria-label="Tok" />
    </div>

</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'

defineProps({
    measurement_units: Array,
    required: true
})

const medicine_store = useMedicineFormStore()
const medicineHungerStation = computed({
  get: () => medicine_store.hunger_situation,
  set: (val) => {
    medicine_store.hunger_situation = val
  }
})
// defineProps({
//     medicine_notes: {
//         type: String,
//         required: true,
//     }
// })
</script>