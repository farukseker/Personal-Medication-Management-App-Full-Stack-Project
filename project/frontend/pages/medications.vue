<template>
<div class="p-4 space-y-4 max-w-md mx-auto">
      <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaçlarım</h1>
            <button 
              @click="$router.push('/settings')"
              class="btn btn-ghost text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
            </div>
        </div>
      <div>
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">Bugün, 13 Mayıs</h2>
          <button 
          class="btn btn-primary btn-sm"
          @click="$router.push('/new_medicine/medicine_name')"
          >+ ilaç ekle</button>
        </div>
        <div class="space-y-3">
          <MedicationPillListItem v-for="medication in my_medication_list" :key="medication.id + 'medication_lcl'" :medication="medication" @load_medication_list="load_my_medication_list" />
        </div>
      </div>
   </div>
</template>

<script setup>
const { $api } = useNuxtApp()

const my_medication_list = ref([])

// const load_my_medication_list = async () => my_medication_list.value = await $api('/medication/medications/')
const load_my_medication_list = async () => my_medication_list.value = await $api('/medication/medications/')
onMounted(load_my_medication_list)
</script>