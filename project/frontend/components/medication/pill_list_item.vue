<template>
<div class="card bg-base-100 shadow">
    <div class="card-body p-3">
        <div class="flex justify-between items-center">
            <div>
                <p class="font-semibold">{{ medication.name}}</p>
                <p class="text-sm text-gray-500">{{ medication.default_dose_amount }} {{ medication.default_dose_unit }}</p>
            </div>
            <div>
                {{ medication.schedules?.length > 0 ? 'Planlandı':''  }}
            </div>
            <div class="flex gap-2">
                <button v-if="medication.schedules?.length === 0" class="btn btn-primary btn-sm">Planla</button>
                <button v-if="medication.schedules?.length === 0" class="btn btn-secondary btn-sm" @click="take_mdicine">Al</button>
                <button class="btn btn-success btn-sm">Düzenle</button>
                <button class="btn btn-outline btn-sm" @click="delete_mdicine(medication.id)">Sil</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
const props = defineProps(['medication'])
const { $api } = useNuxtApp()
const emit = defineEmits(['load_medication_list'])
const on_progress = ref(false)
import dayjs from 'dayjs' // Tarih işlemleri için kullanışlı

const trigger = async () => {
    try{
        const result = await emit('load_medication_list'); // Bu Promise'leri dizi olarak döner
        if (result.length > 0) {
            await result[0]; // ilk dönen Promise varsa beklet
            await nextTick()
        }
    } catch {} finally {
        on_progress.value = false
    }
};

const take_mdicine = async () => {
    try {
        await $api('/medication/medication-logs/create/', {
            method: 'POST',
            body: {
                "medication": props.medication.id,
                "dose": props.medication.default_dose_amount,
                "taken_status": 'taken',
            }
        })
    } catch {} finally {
        await trigger()
        on_progress.value = false
    }
}



const delete_mdicine = async (medication_id) => {
    try {
        await $api(`medication/medications/${medication_id}/`, {
            method: 'DELETE'
        })
    } catch {} finally {
        await trigger()
        on_progress.value = false
    }
}

</script>