<template>
  <dialog ref="modalRef" class="modal">
    <div class="modal-box max-w-2xl">
      <h3 class="font-bold text-lg">{{ isEditing ? 'Planı Düzenle' : 'Yeni Plan Ekle' }}</h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        <input type="date" v-model="schedule.start_date" class="input input-bordered w-full" />
        <input type="date" v-model="schedule.end_date" class="input input-bordered w-full" />

        <select v-model="schedule.frequency" class="select select-bordered w-full">
          <option value="daily">Günlük</option>
          <option value="weekly">Haftalık</option>
          <option value="monthly">Aylık</option>
          <option value="custom">Özel</option>
        </select>

        <div v-if="schedule.frequency === 'custom'" class="col-span-2">
          <input type="number" v-model="schedule.interval" placeholder="Kaç günde bir?" class="input input-bordered w-full" />
        </div>
        
        <div v-if="schedule.frequency === 'monthly'" class="col-span-2">
          <input type="number" v-model="schedule.day_of_month" placeholder="Ayın Kaçıncı Günü" class="input input-bordered w-full" min="1" max="31" />
        </div>

        <div v-if="schedule.frequency === 'weekly'" class="col-span-2">
          <div class="flex gap-2 flex-wrap">
            <label
              v-for="day in weekDays"
              :key="day.value"
              class="btn btn-sm"
              :class="{ 'btn-primary': schedule.days_of_week.includes(day.value), 'btn-outline': !schedule.days_of_week.includes(day.value) }"
            >
              <input type="checkbox" class="hidden" :value="day.value" v-model="schedule.days_of_week" />
              {{ day.label }}
            </label>
          </div>
        </div>

        <div v-if="schedule.frequency === 'monthly'" class="col-span-2">
          <input type="number" v-model="schedule.day_of_month" placeholder="Ayın Kaçıncı Günü" class="input input-bordered w-full" min="1" max="31" />
        </div>

        <input type="number" v-model="schedule.doses_per_period" placeholder="Doz / Periyot" class="input input-bordered w-full" />
        <input type="number" v-model="schedule.dose_amount" placeholder="Doz Miktarı" class="input input-bordered w-full" />
        <input type="text" v-model="schedule.dose_unit" placeholder="Birim" class="input input-bordered w-full" />
      </div>

      <div class="modal-action">
        <form method="dialog" class="flex gap-2">
          <button class="btn">İptal</button>
          <button class="btn btn-primary" @click.prevent="save">{{ isEditing ? 'Güncelle' : 'Ekle' }}</button>
        </form>
      </div>
    </div>
  </dialog>
</template>

<script setup>
import { ref, reactive, defineExpose, computed } from 'vue'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const modalRef = ref()
const store = useNewMdcStore()
const schedule = reactive(blankSchedule())

const isEditing = computed(() => store.editIndex !== null)

const weekDays = [
  { value: 1, label: 'Pzt' },
  { value: 2, label: 'Sal' },
  { value: 3, label: 'Çar' },
  { value: 4, label: 'Per' },
  { value: 5, label: 'Cum' },
  { value: 6, label: 'Cmt' },
  { value: 7, label: 'Paz' },
]

function blankSchedule() {
  return {
    start_date: '',
    end_date: '',
    frequency: 'daily',
    interval: 1,
    days_of_week: [],
    day_of_month: null,
    doses_per_period: 1,
    dose_amount: '',
    dose_unit: '',
  }
}

function open(newSchedule = null) {
  Object.assign(schedule, blankSchedule())
  if (newSchedule) Object.assign(schedule, JSON.parse(JSON.stringify(newSchedule)))
  modalRef.value.showModal()
}

function save() {
  if (store.isOverlapping(schedule)) {
    alert("Çakışan tarih var.")
    return
  }

  const copy = JSON.parse(JSON.stringify(schedule))
  if (isEditing.value) {
    store.updateSchedule(store.editIndex, copy)
  } else {
    store.addSchedule(copy)
  }
  modalRef.value.close()
}

defineExpose({ open })
</script>
