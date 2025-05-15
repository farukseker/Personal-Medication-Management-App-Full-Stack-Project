<template>
  <div class="p-6 space-y-6 bg-base-200 rounded-xl shadow-lg max-w-3xl mx-auto">
    <h2 class="text-2xl font-bold">💊 İlaç Takip Planlayıcı</h2>

    <!-- İlaç Adı -->
    <div>
      <label class="label">İlaç Adı</label>
      <input v-model="form.name" class="input input-bordered w-full" placeholder="Parol, Xanax..." />
    </div>

    <!-- Gün Seçimi -->
    <div>
      <label class="label">Kullanım Günleri</label>
      <div class="flex flex-wrap gap-2">
        <div v-for="day in weekDays" :key="day" class="form-control">
          <label class="cursor-pointer label">
            <input type="checkbox" v-model="form.selectedDays" :value="day" class="checkbox checkbox-primary mr-2" />
            <span class="label-text">{{ day }}</span>
          </label>
        </div>
      </div>
    </div>

    <!-- Doz Ayarları -->
    <div>
      <label class="label">Doz Miktarı ve Birimi</label>
      <div class="flex gap-4">
        <input v-model="form.default_dose_amount" type="number" step="0.1" class="input input-bordered w-1/2" placeholder="1.5" />
        <input v-model="form.default_dose_unit" type="text" class="input input-bordered w-1/2" placeholder="mg / tablet / ml" />
      </div>
    </div>

    <!-- Hatırlatma Saatleri -->
    <div>
      <label class="label">Günlük Hatırlatıcı Saat(ler)i</label>
      <div v-for="(time, index) in form.reminder_times" :key="index" class="flex items-center gap-4 mb-2">
        <input type="time" v-model="form.reminder_times[index]" class="input input-bordered w-full" />
        <button @click="removeTime(index)" class="btn btn-error btn-sm">❌</button>
      </div>
      <button @click="addTime" class="btn btn-accent btn-sm">+ Saat Ekle</button>
    </div>

    <!-- Kademeli Doz Değişimi -->
    <div>
      <label class="label">Kademeli Doz Artış/Azalış</label>
      <div class="flex gap-2">
        <select v-model="form.dose_change.type" class="select select-bordered w-1/2">
          <option value="">Seç</option>
          <option value="increase">Artır</option>
          <option value="decrease">Azalt</option>
        </select>
        <input v-model="form.dose_change.amount" type="number" step="0.1" class="input input-bordered w-1/2" placeholder="0.5" />
      </div>
      <p class="text-sm mt-1 text-gray-400">Her hafta {{ form.dose_change.type === 'increase' ? 'artacak' : 'azalacak' }} miktar</p>
    </div>

    <!-- Kaydet -->
    <button @click="submitForm" class="btn btn-primary w-full">📥 Kaydet</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const weekDays = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']

const form = ref({
  name: '',
  selectedDays: [],
  default_dose_amount: null,
  default_dose_unit: '',
  reminder_times: [],
  dose_change: {
    type: '',
    amount: null,
  },
})

const addTime = () => {
  form.value.reminder_times.push('')
}

const removeTime = (index) => {
  form.value.reminder_times.splice(index, 1)
}

const submitForm = () => {
  console.log('Form verileri:', form.value)
  // Buradan backend'e post edebilirsin
}
</script>
