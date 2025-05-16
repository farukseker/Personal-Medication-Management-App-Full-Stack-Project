<template>
<section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç plan</legend>
    
    <!-- Başlangıç & Bitiş Tarihi -->
    <div class="grid grid-cols-2 gap-2">
      <div>
        <label class="label">Başlangıç Tarihi</label>
        <input start_date type="date" v-model="new_mdc_store.start_date" class="input input-bordered w-full" />
      </div>
      <div>
        <label class="label">Bitiş Tarihi (Opsiyonel)</label>
        <input end_date type="date" v-model="new_mdc_store.end_date" class="input input-bordered w-full" />
      </div>
    </div>

    <!-- Tekrar Sıklığı -->
    <div class="mb-2">
      <label class="label">Tekrar Sıklığı</label>
      <select v-model="new_mdc_store.frequency" class="select select-bordered w-full">
        <option value="daily">Günlük</option>
        <option value="weekly">Haftalık</option>
        <option value="monthly">Aylık</option>
        <option value="custom">Özel</option>
      </select>
    </div>

    <div v-if="new_mdc_store.frequency === 'weekly'" class="join join-vertical">
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Monday" v-model="new_mdc_store.days_of_week" value="Monday" aria-label="Pazartesi" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Tuesday" v-model="new_mdc_store.days_of_week" value="Tuesday" aria-label="Salı" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Wednesday" v-model="new_mdc_store.days_of_week" value="Wednesday" aria-label="Çarşamba" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Thursday" v-model="new_mdc_store.days_of_week" value="Thursday" aria-label="Perşembe" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Friday" v-model="new_mdc_store.days_of_week" value="Friday" aria-label="Cuma" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Saturday" v-model="new_mdc_store.days_of_week" value="Saturday" aria-label="Cumartesi" />
        <input class="join-item btn btn-md justify-start" type="checkbox" name="Sunday" v-model="new_mdc_store.days_of_week" value="Sunday" aria-label="Pazar" />
    </div>
    
    <!-- Ayın Günü (Aylık için) -->
    <div v-if="new_mdc_store.frequency === 'monthly'">
      <label class="label">Ayın Kaçıncı Günü?</label>
      <input v-model="new_mdc_store.day_of_month" type="number" min="1" max="31" class="input input-bordered w-full" />
    </div>

    <!-- Özel Tekrar Aralığı -->
    <div v-if="new_mdc_store.frequency === 'custom'">
      <label class="label">Kaç Günde Bir?</label>
      <input v-model="new_mdc_store.interval" type="number" min="1" class="input input-bordered w-full" />
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
import { useNewMdcStore } from '@/stores/new_mdc_store.js'


const new_mdc_store = useNewMdcStore()
const router = useRouter()

const go_next_page = () => {
    new_mdc_store.form_index = 2
    router.push('/new_medicine/medicine_clock')
}
const go_previous_page = () => {
    new_mdc_store.form_index = 0
    router.push('/new_medicine/medicine_name')
}


definePageMeta({layout: 'newmdc'})
</script>