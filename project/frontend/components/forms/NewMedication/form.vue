<template>
  <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
    <legend class="fieldset-legend">İlaç ekle</legend>
    <form @submit.prevent="">
      <label class="label">İlaç Adı</label>
      <input type="text" class="input w-full" placeholder="ilacın adı" />

      <label class="label">Doz miktarı</label>
      <input type="number" class="input w-full" placeholder="0.5mg, 1mg" />
      <label class="text-sm text-secondary">decimal float destekler</label>

      <label class="label">Doz tipi</label>
      <input type="text" class="input w-full" placeholder="MG|GR|ML|TANE" />
      <button class="btn btn-primary float-end mt-3">Sonraki -></button>
    </form>
  </fieldset>

  <hr class="py-5 bg-cyan-600" />
<section class="bg-base-200 px-4 py-4">
<fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
    <legend class="fieldset-legend">Planlama ekle</legend>
  <form @submit.prevent="handleSubmit" class="p-4 space-y-4 max-w-md mx-auto">
    <!-- Start Date -->
    <div>
      <label class="label">Başlangıç Tarihi</label>
      <input type="date" v-model="form.start_date" class="input input-bordered w-full" />
    </div>

    <!-- End Date -->
    <div>
      <label class="label">Bitiş Tarihi (Opsiyonel)</label>
      <input type="date" v-model="form.end_date" class="input input-bordered w-full" />
    </div>

    <!-- Frequency -->
    <div>
      <label class="label">Tekrar Sıklığı</label>
      <select v-model="form.frequency" class="select select-bordered w-full">
        <option value="daily">Günlük</option>
        <option value="weekly">Haftalık</option>
        <option value="monthly">Aylık</option>
        <option value="custom">Özel</option>
      </select>
    </div>

    <!-- Interval -->
    <div>
      <label class="label">Aralık (gün sayısı)</label>
      <input type="number" min="1" v-model="form.interval" class="input input-bordered w-full" />
    </div>

    <!-- Günlük/Özel Seçimler -->
    <div v-if="form.frequency === 'weekly'">
      <label class="label">Hangi günler?</label>
      <div class="flex flex-wrap gap-2">
        <label v-for="day in weekDays" :key="day.id" class="flex items-center gap-2">
          <input type="checkbox" :value="day.id" v-model="form.days_of_week" class="checkbox" />
          {{ day.name }}
        </label>
      </div>
    </div>

    <div v-if="form.frequency === 'monthly'">
      <label class="label">Ayın kaçıncı günü?</label>
      <input type="number" min="1" max="31" v-model="form.day_of_month" class="input input-bordered w-full" />
    </div>

    <!-- Doses Per Period -->
    <div>
      <label class="label">Periyot başına doz</label>
      <input type="number" min="1" v-model="form.doses_per_period" class="input input-bordered w-full" />
    </div>

    <!-- Dose Amount -->
    <div class="grid grid-cols-2 gap-2">
      <div>
        <label class="label">Doz Miktarı</label>
        <input type="number" step="0.01" v-model="form.dose_amount" class="input input-bordered w-full" />
      </div>

      <div>
        <label class="label">Birim</label>
        <input type="text" v-model="form.dose_unit" class="input input-bordered w-full" />
      </div>
    </div>

    <button type="submit" class="btn btn-primary w-full">Kaydet</button>
  </form>
</fieldset>
</section>
</template>


<script setup>
import { ref } from 'vue'

// Örnek veri – API'den geleceğini varsay
const medications = ref([
  { id: 1, name: 'Parol' },
  { id: 2, name: 'Aferin' },
])

const weekDays = ref([
  { id: 1, name: 'Pzt' },
  { id: 2, name: 'Salı' },
  { id: 3, name: 'Çarş' },
  { id: 4, name: 'Perş' },
  { id: 5, name: 'Cuma' },
  { id: 6, name: 'Cmt' },
  { id: 7, name: 'Pazar' },
])

const form = ref({
  medication: '',
  start_date: '',
  end_date: '',
  frequency: 'daily',
  interval: 1,
  days_of_week: [],
  day_of_month: null,
  doses_per_period: 1,
  dose_amount: null,
  dose_unit: '',
})

const handleSubmit = () => {
  console.log('Form:', form.value)
  // API'ye gönder
}
</script>