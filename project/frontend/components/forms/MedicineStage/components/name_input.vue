<template>
    <label class="label">İlacınızın Adı *</label>
    <input 
        v-model="medicineName"
        type="text" 
        @input="is_name_length_enough = medicineName.length >= 2"
        :class="'input input-sm md:input-md ' + (is_name_length_enough ? '':'outline outline-red-500 focus:outline-red-500 active:outline-red-500')" 
        placeholder="İlacın Adı" 
        id="medicine_name"
        list="medicine_names"
        autocomplete="off"
        />
    <label v-if="!is_name_length_enough" class="label-text-alt">En az 2 karakter yazılmalı</label>
    <datalist v-if="medicineName.length >= 2" id="medicine_names">
      <template>
          <option 
            v-for="_medicine_name in filtered_medicine_names" 
            :key="_medicine_name.id || _medicine_name.name"
            :value="_medicine_name.name" 
          />
      </template>
  </datalist>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'
const { $api } = useNuxtApp()
const medicine_store = useMedicineFormStore()

const medicine_names = ref([])
const load_medicine_names = async () => medicine_names.value = await $api('/medication/medication-compilation-list')
onMounted(load_medicine_names)

const is_name_length_enough = ref(true)

const medicineName = computed({
  get: () => medicine_store.medicine_name,
  set: (val) => {
    medicine_store.medicine_name = val
  }
})

const filtered_medicine_names = computed(() => {
  const name = medicineName.value
  if (!name || typeof name !== 'string' || name.length < 2) return []

  return medicine_names.value.filter(item =>
    item?.name?.toLowerCase().includes(name.toLowerCase())
  )
})

</script>