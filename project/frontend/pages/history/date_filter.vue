<template>
<section class="p-4 space-y-4 max-w-md mx-auto">
    <headersMainHeader :title="$t('index.title')">
        <button class="btn btn-sm btn-success">Rapor Al </button>
    </headersMainHeader>
    <div class="card bg-base-100 sm:shadow mb-3">
        <div class="card-body flex flex-row gap-2 p-0 sm:p-5 w-full justify-between">
            <button class="btn btn-sm btn-outline"
            @click="go('/history/?filter_type=today')"
            >Bugün</button>
            <button class="btn btn-sm btn-outline"
            @click="go('/history/?filter_type=yesterday')"
            >Dün</button>
            <button class="btn btn-sm btn-outline"
            @click="go('/history/?filter_type=week')"
            >Bu hafta</button>
            <button
            class="btn btn-sm btn-outline"
            @click="go('/history/?filter_type=month')"
            >Bu Ay</button>
            <button 
            class="btn btn-sm btn-primary"
            >Özel Tarih</button>
        </div>
    </div>
    <form @submit.prevent="handleSubmit">
        <fieldset class="fieldset">
        <legend
            class="fieldset-legend"
            :class="{ 'text-error': errors.startDate }"
        >
            Filitre başlangıç tarihi ?
        </legend>
        <label class="input w-full" :class="{ 'input-error': errors.startDate }">
            <font-awesome :icon="faCalendarDay" />
            <input
            class="grow"
            type="date"
            v-model="startDate"
            :max="today"
            required
            />
        </label>
        <div v-if="errors.startDate" class="text-sm text-error mt-1">
            {{ errors.startDate }}
        </div>
        </fieldset>

        <fieldset class="fieldset">
        <legend
            class="fieldset-legend"
            :class="{ 'text-error': errors.endDate }"
        >
            Filitre bitiş tarihi ? <span class="text-secondary-content">(opsiyonel)</span>
        </legend>
        <label class="input w-full" :class="{ 'input-error': errors.endDate }">
            <font-awesome :icon="faCalendarDay" />
            <input
            class="grow"
            type="date"
            v-model="endDate"
            :max="today"
            />
        </label>
        <div v-if="errors.endDate" class="text-sm text-error mt-1">
            {{ errors.endDate }}
        </div>
        </fieldset>
        <div class="w-full text-end mt-2">
        <button class="btn btn-primary" type="submit" :disabled="isFormInvalid">
            Filitrele
        </button>
        </div>   
    </form>
    <div v-if="on_loading" class="w-full text-center">
      <span class="loading loading-infinity loading-md"></span>
    </div>
    <div v-else>
        <div class="underline font-semibold text-primary-content text-center animate-pulse" v-if="!(medication_history_list?.length > 0) && isOneTimeSearched">
          <font-awesome :icon="faFolderOpen" />
            liste boş
        </div>
        <div v-for="split_medication_history in medication_history_list">
            <div class="w-full flex gap-2">
              <span class="min-w-fit my-auto">{{ get_readable_date(split_medication_history.date) }}</span>
              <hr class="w-full my-auto">
            </div>
            <div class="flex flex-col gap-2">
              <MedicationPillReminder
                v-for="medication_today in split_medication_history.medication_logs"
                :key="medication_today.id + 3"
                :medication="medication_today"
              />
            </div>
        </div>
    </div>
</section>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
import dayjs from 'dayjs'
import { faCalendarDay } from '@fortawesome/free-solid-svg-icons'
import { faFolderOpen } from '@fortawesome/free-regular-svg-icons'


const { $api } = useNuxtApp()
const { go } = useLocaleRouter()

const startDate = ref('')
const endDate = ref('')
const today = dayjs().format('YYYY-MM-DD')
const medication_history_list = ref([])
const on_loading = ref(false)

const isOneTimeSearched = ref(false) 

const errors = ref({
  startDate: '',
  endDate: '',
})

const get_readable_date = (date) => {
  return dayjs(date).locale('tr').format('DD MMMM YYYY')
}

const validateDates = () => {
  const now = dayjs()
  const start = dayjs(startDate.value)
  const end = endDate.value ? dayjs(endDate.value) : null

  errors.value.startDate = ''
  errors.value.endDate = ''

  if (!startDate.value) {
    errors.value.startDate = 'Başlangıç tarihi zorunludur.'
  } else if (start.isAfter(now, 'day')) {
    errors.value.startDate = 'Başlangıç tarihi bugünden ileri olamaz.'
  }

  if (endDate.value) {
    if (end.isAfter(now, 'day')) {
      errors.value.endDate = 'Bitiş tarihi bugünden ileri olamaz.'
    } else if (end.isBefore(start, 'day')) {
      errors.value.endDate = 'Bitiş tarihi başlangıçtan erken olamaz.'
    }
  }
}

watch([startDate, endDate], validateDates)

const isFormInvalid = computed(() => {
  return !!(errors.value.startDate || errors.value.endDate)
})


const handleSubmit = async () => {
    validateDates() 
    if (isFormInvalid.value) return

    const params = new URLSearchParams({
        date: 'range',
        start_date: startDate.value,
    })

    if (startDate.value && endDate.value) {
        params.append('end_date', endDate.value)
    }

    try{
        on_loading.value = true
        isOneTimeSearched.value = true
        medication_history_list.value = await $api(`/medication/medication-logs/split/?${params.toString()}`)
    } finally {
        on_loading.value = false
    }
}
</script>