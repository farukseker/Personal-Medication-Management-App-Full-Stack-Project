<template>
   <div class="p-4 space-y-4 max-w-md mx-auto">
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
        <div class="underline font-semibold text-primary-content" v-if="!(medication_history_list?.length > 0)">
          liste boş
        </div>
          <form @submit.prevent="handleSubmit" class="bg-base-100 my-3">
            <fieldset class="fieldset">
            <legend class="fieldset-legend">Filitre başlangıç tarihi ?</legend>
            <label class="input w-full">
                <font-awesome :icon="faCalendarDay" />
                <input class="grow" type="date" v-model="startDate" :max="today" required>
            </label>
            </fieldset>

            <fieldset class="fieldset">
            <legend class="fieldset-legend">
                Filitre bitiş tarihi ? <span class="text-secondary-content">(opsiyonel)</span>
            </legend>
            <label class="input w-full">
                <font-awesome :icon="faCalendarDay" />
                <input class="grow" type="date" v-model="endDate" :max="today">
            </label>
            </fieldset>

            <div class="w-full text-end mt-2">
            <button class="btn btn-primary">Filitrele</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const filter_type = ref('date_filter') //today 
const { go } = useLocaleRouter()

import dayjs from 'dayjs'
import { faCalendarDay } from '@fortawesome/free-solid-svg-icons'

const startDate = ref('')
const endDate = ref('')

const today = dayjs().format('YYYY-MM-DD')

const handleSubmit = () => {
  if (!startDate.value) {
    alert('Başlangıç tarihi zorunludur.')
    return
  }

  const start = dayjs(startDate.value)
  const end = dayjs(endDate.value)
  const now = dayjs()

  if (start.isAfter(now, 'day')) {
    alert('Başlangıç tarihi bugünden ileri olamaz.')
    return
  }

  if (endDate.value) {
    if (end.isAfter(now, 'day')) {
      alert('Bitiş tarihi bugünden ileri olamaz.')
      return
    }

    if (end.isBefore(start, 'day')) {
      alert('Bitiş tarihi, başlangıç tarihinden önce olamaz.')
      return
    }
  }

  // 🟢 Başarılı kontrol sonrası devam
  alert('Tarihler geçerli!')
}
</script>