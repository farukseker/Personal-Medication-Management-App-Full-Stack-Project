<template>
<div class="card bg-base-100 shadow">
    <div class="card-body p-3">
        <div class="flex justify-between items-center">
            <div>
            <p class="font-semibold">{{ medication.medication_name }} {{ medication.dose }}{{ medication.unit }}</p>
            <p class="text-sm text-gray-500">Saat {{ medication.time }}  - 1 tablet</p>
            </div>
            <div class="flex gap-2">
            <button class="btn btn-success btn-sm">Aldım</button>
            <button class="btn btn-outline btn-sm">Atla</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
defineProps(['medication'])
</script>