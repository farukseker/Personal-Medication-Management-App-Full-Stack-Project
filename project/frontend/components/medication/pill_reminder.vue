<template>
<div class="card bg-base-100 shadow">
    <div class="card-body p-3">
        <div class="flex justify-between items-center">
            <div>
            <p class="font-semibold">{{ medication.medication_name }} {{ medication.dose }}{{ medication.unit }}</p>
            <p class="text-sm text-gray-500">Saat {{ medication.time }}  - 1 tablet</p>
            </div>
            <div class="flex gap-2">
            <button class="btn btn-success btn-sm" @click="take_pill('taken')">Aldım</button>
            <button class="btn btn-outline btn-sm" @click="take_pill('pass')">Atla</button>
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
    }})

const { $api } = useNuxtApp()
const take_pill = async (status) => await $api('/medication/medication-logs/', {
    method: 'POST',
    body: {
        "medication": medication.medication_id,
        "dose": medication.dose,
        "taken_status": status,
        "dose_time": medication.dose_time_id  
    }
})

</script>