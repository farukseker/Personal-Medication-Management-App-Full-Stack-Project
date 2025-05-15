<template>
<section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">
            <input type="checkbox" class="checkbox checkbox-accent" checked>
            Haftalık Doz planı (Opsiyonel)
        </legend>
        <article class="">
            <ul class="w-full">
                <li class="w-full flex gap-2 mb-2" v-for="(weekly_dose_plan, index) in new_mdc_store.weekly_dose_plans">
                    <strong class="my-auto text-lg">{{ index + 1 }}.</strong>
                    <input class="input w-2/3" type="text" placeholder="Miktar">
                    <select v-model="weekly_dose_plan.dose_unit" class="input w-1/3">
                        <option class="text-gray-600" disabled selected>Ölçek</option>
                        <option v-for="(dose_unit, index) in new_mdc_store.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
                    </select>
                </li>
            </ul>
        </article>
        <button class="btn btn-outline" @click="add_new_weekly_dose_plan">Hafta Ekle</button>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <div class="flex gap-2 w-full">
            <div class="w-full">
                <button class="btn btn-secondary w-full" @click="go_previous_page">Geri</button>
            </div>
            <div class="w-full">
                <button class="btn btn-success w-full">Kaydet</button>
            </div>
        </div>
    </fieldset>
</section>
</template>

<script setup>
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
const new_mdc_store = useNewMdcStore()

const add_new_weekly_dose_plan = () => {
    let default_dose_unit = 'miligram'
    if (new_mdc_store.weekly_dose_plans.length > 0) {
        default_dose_unit = new_mdc_store.weekly_dose_plans[new_mdc_store.weekly_dose_plans.length - 1].dose_unit
    }
    new_mdc_store.weekly_dose_plans.push({
        dose_amount: '',
        dose_unit: default_dose_unit,
        note: '',
        reminder_times: []
    })
}
onMounted(() => {
    if (new_mdc_store.weekly_dose_plans.length === 0) {
        let default_dose_unit = new_mdc_store.dose_unit
        new_mdc_store.weekly_dose_plans.push({
        dose_amount: '',
        dose_unit: default_dose_unit,
        note: '',
        reminder_times: []
    })
    }

})

const del_new_weekly_dose_plan = () => {

}

const router = useRouter()

const go_previous_page = () => {
    new_mdc_store.form_index = 2
    router.push('/new_medicine/medicine_clock')
}
//new_medicine_form_layout/
// weekly_dose_plans
definePageMeta({layout: 'newmdc'})
</script>