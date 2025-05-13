<template>
  <form class="p-4 space-y-4">
    <!-- İlaç Seçimi -->
    <div>
      <label class="label font-bold">İlaç</label>
      <select v-model="form.medication" class="select select-bordered w-full">
        <option disabled value="">İlaç seçin</option>
        <option v-for="med in medications" :key="med.id" :value="med.id">{{ med.name }}</option>
      </select>
    </div>

    <!-- Başlangıç & Bitiş Tarihi -->
    <div class="grid grid-cols-2 gap-2">
      <div>
        <label class="label">Başlangıç Tarihi</label>
        <input v-model="form.start_date" type="date" class="input input-bordered w-full" />
      </div>
      <div>
        <label class="label">Bitiş Tarihi (Opsiyonel)</label>
        <input v-model="form.end_date" type="date" class="input input-bordered w-full" />
      </div>
    </div>

    <!-- Tekrar Sıklığı -->
    <div>
      <label class="label">Tekrar Sıklığı</label>
      <select v-model="form.frequency" class="select select-bordered w-full">
        <option value="daily">Günlük</option>
        <option value="weekly">Haftalık</option>
        <option value="monthly">Aylık</option>
        <option value="custom">Özel</option>
      </select>
    </div>

    <!-- Günler (Haftalık için) -->
    <div v-if="form.frequency === 'weekly'">
      <label class="label">Hangi Günler?</label>
      <div class="flex flex-wrap gap-2">
        <label v-for="day in weekDays" :key="day.id" class="badge cursor-pointer">
          <input type="checkbox" v-model="form.days_of_week" :value="day.id" class="hidden" />
          <span>{{ day.name }}</span>
        </label>
      </div>
    </div>

    <!-- Ayın Günü (Aylık için) -->
    <div v-if="form.frequency === 'monthly'">
      <label class="label">Ayın Kaçıncı Günü?</label>
      <input v-model="form.day_of_month" type="number" min="1" max="31" class="input input-bordered w-full" />
    </div>

    <!-- Özel Tekrar Aralığı -->
    <div v-if="form.frequency === 'custom'">
      <label class="label">Kaç Günde Bir?</label>
      <input v-model="form.interval" type="number" min="1" class="input input-bordered w-full" />
    </div>

    <!-- Günlük Saatler -->
    <div>
      <label class="label font-bold">Günün Saatleri</label>
      <div class="space-y-2">
        <div v-for="(dose, index) in form.dose_times" :key="index" class="flex items-center gap-2">
          <input v-model="dose.time" type="time" class="input input-bordered w-1/3" />
          <input v-model="dose.dose_amount" type="number" step="0.01" class="input input-bordered w-1/3" placeholder="Doz" />
          <input v-model="dose.dose_unit" type="text" class="input input-bordered w-1/3" placeholder="Birim" />
          <button @click.prevent="removeDoseTime(index)" class="btn btn-xs btn-error">✕</button>
        </div>
        <button @click.prevent="addDoseTime" class="btn btn-sm btn-outline w-full">+ Saat Ekle</button>
      </div>
    </div>

    <!-- Periyot başına doz -->
    <div class="grid grid-cols-2 gap-2">
      <div>
        <label class="label">Periyot başına doz</label>
        <input v-model="form.doses_per_period" type="number" min="1" class="input input-bordered w-full" />
      </div>
      <div>
        <label class="label">Toplam Doz Miktarı</label>
        <input v-model="form.dose_amount" type="number" step="0.01" class="input input-bordered w-full" />
      </div>
    </div>

    <div>
      <label class="label">Birim</label>
      <input v-model="form.dose_unit" type="text" class="input input-bordered w-full" />
    </div>

    <!-- Kaydet Butonu -->
    <div class="pt-4">
      <button type="submit" class="btn btn-primary w-full">Kaydet</button>
    </div>
  </form>
</template>

<script setup>
import { reactive } from 'vue'

const medications = [
  { id: 1, name: 'Parol' },
  { id: 2, name: 'Augmentin' },
]

const weekDays = [
  { id: 1, name: 'Pzt' },
  { id: 2, name: 'Sal' },
  { id: 3, name: 'Çar' },
  { id: 4, name: 'Per' },
  { id: 5, name: 'Cum' },
  { id: 6, name: 'Cmt' },
  { id: 7, name: 'Paz' },
]

const form = reactive({
  medication: '',
  start_date: '',
  end_date: '',
  frequency: 'daily',
  interval: 1,
  days_of_week: [],
  day_of_month: null,
  doses_per_period: 1,
  dose_amount: 1.0,
  dose_unit: 'tablet',
  dose_times: [
    { time: '08:00', dose_amount: 1.0, dose_unit: 'tablet' },
  ],
})

function addDoseTime() {
  form.dose_times.push({ time: '', dose_amount: 1.0, dose_unit: '' })
}

function removeDoseTime(index) {
  form.dose_times.splice(index, 1)
}
</script>

<style scoped>
/* Mobilde daha iyi görünüm için */
@media (max-width: 640px) {
  form {
    padding: 1rem;
  }
}
</style>
