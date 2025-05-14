<template>
<div class="card bg-base-100 shadow">
    <div class="card-body p-3">
        <div class="flex justify-between items-center">
            <div>
                <p class="font-semibold">{{ medication.name}}</p>
                <p class="text-sm text-gray-500">{{ medication.default_dose_amount }} {{ medication.default_dose_unit }}</p>
            </div>
            <div>
                {{ medication.schedules.length > 0 ? 'Planlandı':''  }}
            </div>
            <div class="flex gap-2">
                <button v-if="medication.schedules.length === 0" class="btn btn-primary btn-sm">Planla</button>
                <button v-if="medication.schedules.length === 0" class="btn btn-secondary btn-sm">Al</button>
                <button class="btn btn-success btn-sm">Düzenle</button>
                <button class="btn btn-outline btn-sm">Sil</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
defineProps(['medication'])



</script>