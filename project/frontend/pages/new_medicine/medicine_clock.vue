<template>
<section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">
          <input type="checkbox" class="input checkbox checkbox-primary" checked>
          Hatırlatıcı Zamanla
        </legend>
    
    <div>
      <div class="space-y-2 w-full">
        <div v-for="(dose, index) in new_mdc_store.dose_times" :key="index" class="grid grid-cols-5 grid-flow-dense items-center gap-2 w-full">
          <input v-model="dose.time" type="time" class="input input-bordered col-span-2" />
          <input v-model="dose.dose_amount" type="number" step="0.01" class="input input-bordered col-span-1" placeholder="Doz" />
          <select v-model="dose.dose_unit" class="input col-span-1">
                <option class="text-gray-600" disabled selected>Ölçek</option>
                <option v-for="(dose_unit, index) in new_mdc_store.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
            </select>
          <button @click.prevent="removeDoseTime" class="btn btn-error col-span-1">✕</button>
        </div>
        <button @click.prevent="addDoseTime" class="btn btn-outline w-full">+ Saat Ekle</button>
      </div>
    </div>

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
const dose_times = ref([])

// dose_times
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
const new_mdc_store = useNewMdcStore()

function addDoseTime() {
  new_mdc_store.dose_times.push({ time: '', dose_amount: 1.0, dose_unit: '' })
}

onMounted(() => {
  if (new_mdc_store.dose_times.length === 0) {
    new_mdc_store.dose_times.push({ time: '10:30', dose_amount: 1.0, dose_unit: new_mdc_store.dose_unit})
  }
})

function removeDoseTime(index) {
  new_mdc_store.dose_times.splice(index, 1)
}

const router = useRouter()

const go_next_page = () => {
    new_mdc_store.form_index = 3
    router.push('/new_medicine/medicine_dose')
}
const go_previous_page = () => {
    new_mdc_store.form_index = 1
    router.push('/new_medicine/medicine_plan')
}


const plan_day = ref([])
const frequency = ref('daily')
//new_medicine_form_layout
definePageMeta({layout: 'newmdc'})
</script>