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
                    <button class="btn btn-error" @click="del_new_weekly_dose_plan(index)">X</button>
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
                <button class="btn btn-success w-full" @click="save_medicine">Kaydet</button>
            </div>
        </div>
    </fieldset>
</section>
</template>

<script setup>
import { useNewMdcStore } from '@/stores/new_mdc_store.js'
const new_mdc_store = useNewMdcStore()
const { $api } = useNuxtApp()

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

const get_day_index_from_list = (list) => {
    let day_indexs = [] 
    list.forEach(e => {
        day_indexs.push(
            {
                "Monday":0,
                "Tuesday":1,
                "Wednesday":2,
                "Thursday":3,
                "Friday":4,
                "Saturday":5,
                "Sunday":6,
            }[e]
        )
    })
    return day_indexs
}


import dayjs from 'dayjs' // Tarih işlemleri için kullanışlı



const save_medicine = async () =>{
    await $api('/medication/medications/create/', {
        method: 'POST',
        body: {
            name: new_mdc_store.medicine_name,
            default_dose_amount: new_mdc_store.medicine_dose_amount,
            default_dose_unit: new_mdc_store.medicine_dose_unit, 
            days_of_week: get_day_index_from_list(new_mdc_store.days_of_week),
            "schedules": [
                {
                    "start_date": dayjs(new_mdc_store.start_date).format('YYYY-MM-DD'),
                    "end_date": dayjs(new_mdc_store.end_date).format('YYYY-MM-DD'),
                    "frequency": new_mdc_store.frequency,
                    "interval": new_mdc_store.interval,
                    "day_of_month": new_mdc_store.day_of_month,
                    "doses_per_period": new_mdc_store.doses_per_period,
                    "dose_amount": new_mdc_store.medicine_dose_amount,
                    "dose_unit": new_mdc_store.medicine_dose_unit,
                }
            ],
        "dose_times": new_mdc_store.dose_times
        }
    })
    
    //    "name": "salofalk",
    //     "dose_times": [
    //     {"time":"10:30", "dose_amount":12, "dose_unit": "mg"},
    //     {"time":"10:40", "dose_amount":12, "dose_unit": "mg"},
    // ],
    // "is_active": True,
    // "default_dose_amount": "1.00",
    // "default_dose_unit": "mg",
    // "days_of_week": [0,1,2,3,4,5,6],

    // "schedules": [
    //         {
    //             "start_date": "2025-04-12",
    //             "end_date": "2025-05-13",
    //             "frequency": "daily",
    //             "interval": 1,
    //             "day_of_month": 0,
    //             "doses_per_period": 3,
    //             "dose_amount": "2.00",
    //             "dose_unit": "mg",
    //             "medication": 1,
    //         }
    // ],

    // "default_dose_amount": 2,
    // "default_dose_unit": "mililitre", 
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

const del_new_weekly_dose_plan = (index) => {
    new_mdc_store.weekly_dose_plans.splice(index, 1)
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