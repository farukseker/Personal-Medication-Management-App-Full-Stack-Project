<template>
<section class="flex flex-col gap-4">
    <!--fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Tara</legend>
    </fieldset-->
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç bilgileri</legend>
        <div
        class="w-full bg-base-200 "
            >
        <input 
            type="text"
            class="input w-full"
            v-model="new_mdc_store.medicine_name"
            @focusin="on_focus = true"
            @focusout="() => setTimeout(() => { on_focus = false }, 200)"
            placeholder="İlaç adı">
            <div v-if="on_focus" class="max-h-[40vh]">
                <ul class="px-3 py-2">
                    <li 
                    class="py-1 text-base cursor-pointer"
                    v-for="result in results"
                    @mousedown.prevent="apply_selected_mdc(result)"
                    >
                        <strong>{{result.name}}</strong>
                    </li>
                </ul>
            </div>
        </div>
        <article class="flex mt-2 gap-2">
            <input class="input w-2/3" type="number" v-model="new_mdc_store.medicine_dose_amount" placeholder="İlaç tek ünite değeri">
            <select v-model="new_mdc_store.medicine_dose_unit" class="input w-1/3">
                <option class="text-gray-600" disabled selected>Ölçek</option>
                <option v-for="(dose_unit, index) in new_mdc_store.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
            </select>
        </article>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Kullanım</legend>
        <article class="flex mt-2 gap-2">
            <input class="input w-2/3" type="number" v-model="new_mdc_store.dose_amount" placeholder="İlaç tek ünite değeri">
            <select v-model="new_mdc_store.dose_unit" class="input w-1/3">
                <option class="text-gray-600" disabled selected>Ölçek</option>
                <option v-for="(dose_unit, index) in new_mdc_store.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
            </select>
        </article>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç Notu</legend>
        <textarea v-model="new_mdc_store.medicine_notes" class="input w-full min-h-32"></textarea>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <button class="btn btn-primary" @click="go_next_page">Devam et</button>
    </fieldset>
</section>
</template>

<script setup>
const on_focus = ref(false)
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const new_mdc_store = useNewMdcStore()
const router = useRouter()

new_mdc_store.vaild_form_1 = new_mdc_store.medicine_name.length > 0 && new_mdc_store.dose_amount !== '' && new_mdc_store.dose_unit !== ''

const apply_selected_mdc = (mdc) => {
  new_mdc_store.medicine_name = mdc.name
  new_mdc_store.medicine_dose_unit = mdc.unit
  new_mdc_store.medicine_dose_amount = mdc.value
  on_focus.value = false
  results.value = []
}

const go_next_page = () => {
    new_mdc_store.form_index = 1
    router.push('/new_medicine/medicine_plan')
}
const fetchData = async () => {
  const response = await fetch('/auto_comp.json')
  const data = await response.json()
  return data
}
const searchByName = async (query) => {
  const data = await fetchData()
  const lower = query.toLowerCase()

  return data.filter(item => item.name.toLowerCase().includes(lower))
}
const results = ref([])

watch(
  () => new_mdc_store.medicine_name, // getter fonksiyonu olarak vermelisin
  async (val) => {
    if (val.length > 1) {
      const data = await searchByName(val)
      results.value = data
    } else {
      results.value = []
    }
  }
)
definePageMeta({layout: 'newmdc'})
</script>