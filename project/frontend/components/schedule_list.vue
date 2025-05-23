<template>
  <div>
    <div v-if="store.schedules.length" class="mt-6 space-y-4">
      <div
        v-for="(schedule, index) in store.sortedSchedules"
        :key="index"
        class="p-4 bg-base-200 rounded-xl shadow flex justify-between"
      >
        <div>
          <h3 class="font-bold text-lg">{{ schedule.frequency?.toUpperCase() }} Planı</h3>
          <p>{{ schedule.start_date }} - {{ schedule.end_date || 'Süresiz' }}</p>
        </div>
        <div class="flex gap-2">
          <button class="btn btn-sm btn-outline" @click="$router.push(`/new_medicine/medicine_plan_form?schedule_index=${index}`)">Düzenle</button>
          <button class="btn btn-sm btn-error" @click="store.removeSchedule(index)">Sil</button>
        </div>
      </div>
    </div>
    <MedicinePlanForm ref="modalRef" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const modalRef = ref()
const store = useNewMdcStore()

function add() {
  store.resetEditIndex()
  modalRef.value.open()
}

function edit(index) {
  store.setEditIndex(index)
  modalRef.value.open(store.schedules[index])
}
</script>
