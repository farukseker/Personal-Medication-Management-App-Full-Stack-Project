<template>
    <client-only>
        <forms-medicine-stage-components-save-btn-bar :enable="!false" @send="send_medicine"/>
    </client-only>
    <section class="w-full flex flex-col gap-4 px-4 pt-2 font-mono">
        <fieldset class="w-full fieldset bg-gradient-to-b border-b-2 shadow-md from-base-300 to-base-100 border-base-300 rounded-box p-4">
            <legend class="fieldset-legend font-bold">İlaç bilgileri</legend>
            <section class="flex flex-col-reverse gap-4 lg:flex-row h-full">
                <article class="w-full h-full flex-1">
                    <forms-medicine-stage-components-name-input />
                    <forms-medicine-stage-components-note-input />
                    <forms-medicine-stage-components-hunger-situation />
                    <forms-medicine-stage-components-scale-types :measurement_units="measurement_units"  />
                    <div v-if="medicine_store.scale_type === 'scale'" class="w-full flex gap-2">
                        <forms-medicine-stage-components-medicine-unit-input 
                            :measurement_units="measurement_units"
                        />
                    </div>
                    <forms-medicine-stage-components-often-select />
                    <forms-medicine-stage-components-reminder-settings />
                    <forms-medicine-stage-components-start-end-date-input />
                </article>
                <article class="w-full h-full flex-1 my-auto md:my-4">
                    <div class="m-auto cursor-pointer w-full h-[20vh] md:h-[36vh] lg:h-[60vh] border-2 border-dashed border-gray-400 bg-primary-content rounded md:rounded-lg flex">
                        <span class="m-auto text-4xl select-none">+</span>
                    </div>
                </article>
            </section>
        </fieldset>
        <article class="flex flex-col md:flex-row gap-6">
            <fieldset v-if="medicine_store.scale_type === 'special'" class="w-full fieldset bg-base-300 border-base-300 rounded-box p-4">
                <legend class="fieldset-legend font-bold">İlaç tarifesi</legend>
                <div class="flex gap-2 flex-col ">
                    <form @submit.prevent="add_increasing" class="w-full flex flex-col xl:flex-row gap-2">
                        <forms-medicine-stage-components-medicine-unit-input 
                            :measurement_units="measurement_units"
                        />
                        <forms-medicine-stage-components-loop-input />
                        <div class="flex flex-col">
                            <span class="h-2 md:h-10"></span>
                            <button class="btn btn-sm md:btn-md btn-success text-white" type="submit">Ekle</button>
                        </div>
                    </form>
                    <div class="flex w-full">
                        <forms-medicine-stage-components-use-instructions-table @del_increasing="del_increasing" />
                    </div>
                </div>
            </fieldset>
        </article>
    </section>
</template>

<script setup>
const toast = useToast()
//['admin', 'super_admin'].includes(user_type)
import dayjs from 'dayjs' // Tarih işlemleri için kullanışlı
const { $api } = useNuxtApp()
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'
const medicine_store = useMedicineFormStore()

const measurement_units = ref([
    {
        param: "ui",
        value:"UI"
    },
    {
        param: "microgram",
        value:"MCG"
    },
    {
        param: "miligram",
        value:"MG"
    },
    {
        param: "gram",
        value:"GR"
    },
    {
        param: "mililitre",
        value:"ML"
    },
    {
        param: "pieces",
        value:"Tane"
    },
    {
        param: "amp",
        value:"Ampül"
    },
    {
        param: "drop",
        value:"Damla"
    }
])

const eng_to_tr_day_names = ref({
    "day": 'Günde',
    "week": 'Haftada',
    "month": 'Ayda',
    "year": 'Yılda'
})


const del_increasing = (increasing_index) => medicine_store.increasing_ranges.splice(increasing_index, 1) 

const add_increasing = () => {
    if (!(medicine_store.increasing_range == null || isNaN(medicine_store.increasing_range)) && medicine_store.increasing_range > 0) {
        // Eğer daha önce aralık eklendiyse, onun end tarihini al
        let real_start = dayjs(medicine_store.start_date)
        if (medicine_store.increasing_ranges.length > 0) {
            const last_range = medicine_store.increasing_ranges[medicine_store.increasing_ranges.length - 1]
            real_start = dayjs(last_range.end).add(1, 'day') // Bir gün sonra başla
        }
        
        let end_date
        switch (medicine_store.direction_range_type) {
            case 'day':
                end_date = real_start.add(medicine_store.direction_range, 'day')
                break
            case 'week':
                end_date = real_start.add(medicine_store.direction_range, 'week')
                break
            case 'month':
                end_date = real_start.add(medicine_store.direction_range, 'month')
                break
            case 'year':
                end_date = real_start.add(medicine_store.direction_range, 'year')
                break
            default:
                alert("Geçersiz zaman türü")
                return;
        }

        medicine_store.increasing_ranges.push({
            start: real_start,
            end: end_date,
            weight_type: medicine_store.weight_type,
            range: medicine_store.direction_range,
            range_type_tr_name: eng_to_tr_day_names.value[medicine_store.direction_range_type],
            range_type: medicine_store.direction_range_type,
            label: `${medicine_store.direction_range} ${medicine_store.direction_range_type}`,
            increasing: medicine_store.increasing_range,
        })
        console.log(medicine_store.increasing_ranges)
        
        if (medicine_store.increasing_ranges.length >= 2) {
            const f = medicine_store.increasing_ranges[medicine_store.increasing_ranges.length - 1].increasing
            const s = medicine_store.increasing_ranges[medicine_store.increasing_ranges.length - 2].increasing
            const diff = Math.abs(f - s)
            const isIncreasing = f > s
            medicine_store.increasing_range = isIncreasing ? f + diff : f - diff
        } else {
            medicine_store.increasing_range = 0
        }
    }

}

const api_query = ref({}) 
const success_msg = ref({title: "İlaç eklendi",  description:"İlacınız başraıyla eklendi"})


const send_medicine = async () => {
    const stages = []
    if (medicine_store.scale_type === 'scale'){
        stages.push({
            "unit": medicine_store.increasing_range,
            "unit_type": medicine_store.weight_type,
            "range_length": 1,
            "range_type": 'end',
            "range_start_date": medicine_store.start_date,
            "range_end_date": medicine_store.end_date,
        })
    } else {
        medicine_store.increasing_ranges.forEach(obj => {
            stages.push({
                "unit": obj.increasing,
                "unit_type": obj.weight_type,
                "range_length": obj.range,
                "range_type": obj.range_type,
                "range_start_date": obj.start,
                "range_end_date": obj.end
            })
        })
    }
    
    api_query.value = {
        "name": medicine_store.medicine_name,
        "notes": medicine_store.medicine_notes,
        "hunger_situation": medicine_store.hunger_situation,
        "start_date": medicine_store.start_date,
        "end_date": medicine_store.end_date,
        "stages": stages,
        "often": medicine_store.often_list
    }
    var response = await $api('/medication/create', {
        method: 'POST',
        body: toRaw(api_query.value)
    })
    if (response){
        toast.add(success_msg.value)
    }
}

</script>

<style>
input[type="text"] {
    @apply w-full
}
</style>