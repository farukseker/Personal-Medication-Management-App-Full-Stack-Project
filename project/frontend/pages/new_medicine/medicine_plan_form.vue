<template>

<header class="flex bg-base-300 p-4 sticky top-0 z-10 rounded-b-md shdow max-w-md mx-auto">
    <div 
    @click="go('/new_medicine/medicine_plan')"
    class="w-[36px] my-auto">
        <font-awesome :icon="faArrowLeft" />
    </div>
    <div class="w-full my-auto">Plan adı ve sırası </div>
    <div class="w-fit">
        <button class="btn btn-sm btn-primary text-white" @click="saveSchedule" :disabled="!form_is_vaild()">Kaydet</button>
    </div>
</header>
<fieldset class="fieldset  rounded-box w-xs p-4 max-w-md mx-auto">
    <legend class="fieldset-legend text-xl">Plan 1.</legend>
    <article class="flex flex-col gap-4">
        <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
            <legend class="fieldset-legend font-bold">Zamanlama</legend>
            <div>
                <label>Plan Başlangıç tarihi</label>  
                <input v-model="schedule.start_date" type="date" class="input w-full" placeholder="My awesome page" />
                <p class="label">ilaç alım tarihi başlangıcı veya doz planması için gerekli</p>
            </div>
            <div>
                <label>Plan Bitiş tarihi</label>  
                <input v-model="schedule.end_date" type="date" class="input w-full" placeholder="My awesome page" />
                <p class="label">bitiş tarihi boş bırakılabilir. </p>
            </div>
        </fieldset>

        <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box gap-4 p-4">
            <legend class="fieldset-legend font-bold">Takip</legend>
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
                <label>Hangi günler kullanılacak</label>
                <div class="flex gap-2 flex-wrap">
                <label
                    v-for="day in weekDays"
                    :key="day.value"
                    class="btn btn-sm"
                    :class="{ 'btn-primary': schedule.days_of_week.includes(day.value), 'btn-outline': !schedule.days_of_week.includes(day.value) }"
                >
                    <input type="checkbox" class="hidden" :value="day.value" v-model="schedule.days_of_week" />
                    <span class="visible">
                        {{ day.label }}
                    </span>
                </label>
                </div>
            </div>
        </fieldset>

    <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Kullanım</legend>
        <article class="flex mt-2 gap-2">
            <div class="w-2/3 flex flex-col">
                <label class="label">Miktar</label>
                <input class="input w-full" type="number" v-model="schedule.dose_amount" placeholder="İlaç tek ünite değeri">
            </div>
            <div class="w-1/3 flex flex-col">
                <label class="label opacity-0">Miktar</label>
                <select v-model="scheduleStore.dose_unit" class="input w-full">
                    <option class="text-gray-600" disabled selected>Ölçek</option>
                    <option v-for="(dose_unit, index) in scheduleStore.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
                </select>
            </div>
        </article>
    </fieldset>

    <fieldset class="w-full bg-base-200 fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">
          <input type="checkbox" class="input checkbox checkbox-primary" checked>
          Hatırlatıcı Zamanla
        </legend>
        <div>
            <div class="space-y-2 w-full">
                <div v-for="(dose, index) in schedule.dose_times" :key="index" class="grid grid-cols-5 grid-flow-dense items-center gap-2 w-full">
                <input v-model="dose.time" type="time" class="input input-bordered col-span-2" />
                <input v-model="dose.dose_amount" type="number" step="0.01" class="input input-bordered col-span-1" placeholder="Doz" />
                <select v-model="dose.dose_unit" class="input col-span-1">
                        <option class="text-gray-600" disabled selected>Ölçek</option>
                        <option v-for="(dose_unit, index) in scheduleStore.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
                    </select>
                <button @click.prevent="removeDoseTime(index)" class="btn btn-error col-span-1">✕</button>
                </div>
                <button @click.prevent="addDoseTime" class="btn btn-outline w-full">+ Saat Ekle</button>
            </div>
        </div>
    </fieldset>

    <div class="w-full flex gap-2">
        <button class="btn btn-secondary w-1/2" 
        @click="go('/new_medicine/medicine_plan')"
        >İptal</button>
        <button class="btn btn-primary w-1/2" @click="saveSchedule" :disabled="!form_is_vaild()">Kaydet</button>
    </div>

</article>
</fieldset>
</template>

<script setup>
import { faCalendar, faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
const route = useRoute();

const schedule_index = route.query.schedule_index || null;

const scheduleStore = useNewMdcStore()

const schedule = ref({
  start_date: '',
  end_date: null,
  frequency: 'daily',
  interval: 1,
  days_of_week: [],
  day_of_month: null,
  doses_per_period: 1,
  dose_amount: 1,
  dose_unit: '',
  dose_times: []
})


const weekDays = [
  { value: 1, label: 'Pzt' },
  { value: 2, label: 'Sal' },
  { value: 3, label: 'Çar' },
  { value: 4, label: 'Per' },
  { value: 5, label: 'Cum' },
  { value: 6, label: 'Cmt' },
  { value: 7, label: 'Paz' },
]

const form_is_vaild = () => {
    return schedule.value.start_date && schedule.value.dose_amount
}

onMounted(() => {
    if (schedule_index && scheduleStore.schedules.length > 0 && scheduleStore.schedules[schedule_index]){
        Object.assign(schedule.value, scheduleStore.schedules[schedule_index])
    }
})

// dose_times

const saveSchedule = () => {
  if (scheduleStore.isOverlapping(schedule.value, schedule_index)) {
    alert("Aynı tarihlerde başka bir plan zaten var. Lütfen tarihleri değiştir.")
    return
  }
  if (schedule_index === null) {
    scheduleStore.addSchedule(schedule.value)
  } else {
    scheduleStore.updateSchedule(schedule_index, schedule.value)
  }
  // plan a yönlendir
  go('/new_medicine/medicine_plan')
}

const removeSchedule = (index) => {
  scheduleStore.removeSchedule(index)
}

const addDoseTime = () => {
    let default_dose_unit = schedule.value.dose_times.length > 0 ? schedule.value.dose_times[schedule.value.dose_times.length - 1].dose_unit : scheduleStore.dose_unit
    schedule.value.dose_times.push({ time: '', dose_amount: 1.0, dose_unit: default_dose_unit })
}

onMounted(() => {
  if (schedule.value.dose_times.length === 0) {
    let default_dose_unit = scheduleStore.dose_unit
    schedule.value.dose_times.push({ time: '10:30', dose_amount: 1.0, dose_unit: default_dose_unit})
  }
})

const removeDoseTime = (index) => {
  schedule.value.dose_times.splice(index, 1)
}

</script>