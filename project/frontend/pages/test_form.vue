<template>
  <!-- Modal Toggle Button -->
  <button class="btn btn-primary" @click="openNewModal">+ Yeni Plan Ekle</button>
  <div v-if="schedules.length" class="mt-6 space-y-4">
    <div v-for="(schedule, index) in sortedSchedules" :key="index" class="p-4 bg-base-200 rounded-xl shadow flex justify-between">
      <div>
        <h3 class="font-bold text-lg">{{ schedule.frequency.toUpperCase() }} Planı</h3>
        <p>{{ schedule.start_date }} - {{ schedule.end_date || 'Süresiz' }}</p>
      </div>
      <div class="flex gap-2">
        <button class="btn btn-sm btn-outline" @click="openEditModal(index)">Düzenle</button>
        <button class="btn btn-sm btn-error" @click="removeSchedule(index)">Sil</button>
      </div>
    </div>
  </div>

  <!-- Modal -->
  <dialog ref="modalRef" class="modal">
    <div class="modal-box max-w-2xl">
      <h3 class="font-bold text-lg">{{ editIndex === null ? 'Yeni Plan Ekle' : 'Planı Düzenle' }}</h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        <!-- Başlangıç / Bitiş Tarihi -->
        <input type="date" v-model="currentSchedule.start_date" class="input input-bordered w-full" />
        <input type="date" v-model="currentSchedule.end_date" class="input input-bordered w-full" />

        <!-- Sıklık -->
        <select v-model="currentSchedule.frequency" class="select select-bordered w-full">
          <option value="daily">Günlük</option>
          <option value="weekly">Haftalık</option>
          <option value="monthly">Aylık</option>
          <option value="custom">Özel</option>
        </select>

        <!-- Özel / Haftalık / Aylık Koşulları -->
        <div v-if="currentSchedule.frequency === 'custom'" class="col-span-2">
          <input type="number" v-model="currentSchedule.interval" placeholder="Kaç günde bir?" class="input input-bordered w-full" />
        </div>

        <div v-if="currentSchedule.frequency === 'weekly'" class="col-span-2">
          <div class="flex gap-2 flex-wrap">
            <label
              v-for="day in weekDays"
              :key="day.value"
              class="btn btn-sm"
              :class="{ 'btn-primary': currentSchedule.days_of_week.includes(day.value), 'btn-outline': !currentSchedule.days_of_week.includes(day.value) }"
            >
              <input type="checkbox" class="hidden" :value="day.value" v-model="currentSchedule.days_of_week" />
              {{ day.label }}
            </label>
          </div>
        </div>

        <div v-if="currentSchedule.frequency === 'monthly'" class="col-span-2">
          <input type="number" v-model="currentSchedule.day_of_month" placeholder="Ayın Kaçıncı Günü" class="input input-bordered w-full" min="1" max="31" />
        </div>

        <!-- Doz Bilgileri -->
        <input type="number" v-model="currentSchedule.doses_per_period" placeholder="Doz / Periyot" class="input input-bordered w-full" />
        <input type="number" v-model="currentSchedule.dose_amount" placeholder="Doz Miktarı" class="input input-bordered w-full" />
        <input type="text" v-model="currentSchedule.dose_unit" placeholder="Birim" class="input input-bordered w-full" />
      </div>

      <!-- Modal Footer -->
      <div class="modal-action">
        <form method="dialog" class="flex gap-2">
          <button class="btn">İptal</button>
          <button class="btn btn-primary" @click.prevent="saveSchedule">
            {{ editIndex === null ? 'Ekle' : 'Güncelle' }}
          </button>
        </form>
      </div>
    </div>
  </dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'

const schedules = ref([])
const modalRef = ref()
const editIndex = ref(null)

const blankSchedule = () => ({
  start_date: '',
  end_date: '',
  frequency: 'daily',
  interval: 1,
  days_of_week: [],
  day_of_month: null,
  doses_per_period: 1,
  dose_amount: '',
  dose_unit: ''
})

function frequencyLabel(value) {
  const labels = {
    daily: 'Günlük',
    weekly: 'Haftalık',
    monthly: 'Aylık',
    custom: 'Özel'
  }
  return labels[value] || value
}


const currentSchedule = reactive(blankSchedule())

const weekDays = [
  { value: 1, label: 'Pzt' },
  { value: 2, label: 'Sal' },
  { value: 3, label: 'Çar' },
  { value: 4, label: 'Per' },
  { value: 5, label: 'Cum' },
  { value: 6, label: 'Cmt' },
  { value: 7, label: 'Paz' }
]


function openNewModal() {
  Object.assign(currentSchedule, blankSchedule())
  editIndex.value = null
  modalRef.value.showModal()
}

function openEditModal(index) {
  Object.assign(currentSchedule, JSON.parse(JSON.stringify(schedules.value[index])))
  editIndex.value = index
  modalRef.value.showModal()
}

function editSchedule(schedule) {
  const index = schedules.value.indexOf(schedule)
  if (index !== -1) {
    editIndex.value = index
    currentSchedule = JSON.parse(JSON.stringify(schedule))
    modalRef.value.showModal()
  }
}

function deleteSchedule(schedule) {
  const index = schedules.value.indexOf(schedule)
  if (index !== -1) schedules.value.splice(index, 1)
}
const sortedSchedules = computed(() =>
  [...schedules.value].sort((a, b) => new Date(a.start_date) - new Date(b.start_date))
)

function saveSchedule() {
  if (isOverlapping(currentSchedule, schedules.value)) {
    alert("Aynı tarihlerde başka bir plan zaten var. Lütfen tarihleri değiştir.")
    return
  }

  const newItem = JSON.parse(JSON.stringify(currentSchedule))
  if (editIndex.value === null) {
    schedules.value.push(newItem)
  } else {
    schedules.value[editIndex.value] = newItem
  }
  modalRef.value.close()
}

function removeSchedule(index) {
  schedules.value.splice(index, 1)
}

function isOverlapping(newSchedule, schedules) {
  const startA = new Date(newSchedule.start_date)
  const endA = newSchedule.end_date ? new Date(newSchedule.end_date) : null

  return schedules.some((s, i) => {
    // Edit moddaysa aynı index'i atla
    if (editIndex.value !== null && i === editIndex.value) return false

    const startB = new Date(s.start_date)
    const endB = s.end_date ? new Date(s.end_date) : null

    // Bitiş tarihi yoksa hep açık say → sonsuza kadar geçerli gibi davran
    const rangeA_end = endA || new Date('9999-12-31')
    const rangeB_end = endB || new Date('9999-12-31')

    // Çakışma kontrolü (A ∩ B ≠ ∅)
    return startA <= rangeB_end && startB <= rangeA_end
  })
}
</script>
