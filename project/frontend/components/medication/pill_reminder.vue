<template>
<div class="card bg-base-100 shadow">
    <div class="card-body p-3">
        <div class="flex justify-between items-center">
            <div>
            <p class="font-semibold">
                {{ medication.medication_name }}
                <span v-if="medication.taken_status" class="text-gray-500">{{ medication.taken_status === 'taken' ? 'Alındı':'Pas' }}</span>
            </p>
            <p class="text-sm text-gray-500">Saat {{ medication.time.slice(0, 5) }}  - {{ medication.dose }}{{ medication.unit }}</p>
            </div>
            <div class="flex gap-2">
            <button :disabled="on_progress" v-if="medication.taken_status ? !['taken', 'pass'].includes(medication.taken_status) : true" class="btn btn-success btn-sm" @click="take_pill('taken')">
                <span v-if="!on_progress">Aldım</span>
                <span v-else class="loading loading-spinner loading-sm"></span>
            </button>
            <button :disabled="on_progress" v-if="medication.taken_status ? !['taken', 'pass'].includes(medication.taken_status) : true" class="btn btn-outline btn-sm" @click="take_pill('pass')">
                <span v-if="!on_progress">Atla</span>
                <span v-else class="loading loading-spinner loading-sm"></span>
            </button>
            <button :disabled="on_progress" v-else class="btn btn-error btn-sm" @click="delete_pill">
                <span v-if="!on_progress">Sil</span>
                <span v-else class="loading loading-spinner loading-sm"></span>
            </button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
const { medication } = defineProps({
    medication: {
        type: Object,
        required: true
    }
})
const emit = defineEmits(['load_medication'])
const { $api } = useNuxtApp()

const on_progress = ref(false)

const trigger = async () => {
    try{
        const result = await emit('load_medication'); // Bu Promise'leri dizi olarak döner
        if (result.length > 0) {
            await result[0]; // ilk dönen Promise varsa beklet
            await nextTick()
        }
    } catch {} finally {
        on_progress.value = false
    }
};

const take_pill = async (status) => {
    try {
        if (on_progress.value === true) {return;}
        on_progress.value = true
        await $api('/medication/medication-logs/create/', {
            method: 'POST',
            body: {
                "medication": medication.medication_id,
                "dose": medication.dose,
                "taken_status": status,
                "dose_time": medication.dose_time_id  
            }
        })
    } catch {} finally {
        // await emit('load_medication')
        await trigger()
        on_progress.value = false
    }

}


// /medication/medication-logs/29/
const delete_pill = async () => {
    try {
        if (on_progress.value === true) {return;}
        on_progress.value = true
        await $api(`/medication/medication-logs/${medication.id}/`, {
        method: 'DELETE'
        })
    } catch {} finally {
        await trigger()
        on_progress.value = false
    }
}

</script>