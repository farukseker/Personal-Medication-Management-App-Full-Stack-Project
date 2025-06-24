<template>
    <section class="px-4 space-y-4 max-w-md mx-auto">
        <header class="flex">
            <button 
                class="btn btn-ghost ps-0 text-xl py-2"
                @click="go('/tab/weight_tracking')"
                >
                <font-awesome :icon="faArrowLeft" />
            </button>
            <h1 class="text-xl font-bold m-auto text-primary">Kilo ekle</h1>
        </header>
        <form @submit.prevent="addWeight">
            <article class="flex flex-col gap-4">
                <fieldset class="w-full fieldset shadow rounded-box p-2">
                    <legend class="fieldset-legend font-bold text-lg text-pretty text-secondary-content">Kilo bilgilerinizi giriniz</legend>
                    <label class="input w-full">
                        <font-awesome :icon="faCalendar" />
                        <input required v-model="newDate" type="date" class="grow" placeholder="Tarih">
                    </label>
                    <label class="input w-full">
                        <font-awesome :icon="faWeight" />
                        <input required v-model="newWeight" type="number" class="grow" placeholder="Kilo">
                    </label>
                </fieldset>
                <fieldset class="w-full fieldset shadow rounded-box p-2">
                    <div class="grid grid-cols-2 gap-2">
                        <button type="button" @click="go('/tab/weight_tracking')" class="btn btn-secondary">Geri</button>
                        <button type="submit" class="btn btn-primary">Ekle</button>
                    </div>
                </fieldset>
            </article>
        </form>
    </section>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
import dayjs from 'dayjs'
import { 
    faCalendar,
    faWeight,
    faArrowLeft,
} from '@fortawesome/free-solid-svg-icons'

const { go } = useLocaleRouter()
const store = useWeightEntryStore()

const newWeight = ref(null)
const newDate = ref(null)

onMounted(() => {
    const today = dayjs().format('YYYY-MM-DD')
    newDate.value = today
})

const addWeight = () => {
  store.addEntry(newWeight.value, newDate.value)
  newWeight.value = null
  newDate.value = null
  go('/tab/weight_tracking')
}
</script>