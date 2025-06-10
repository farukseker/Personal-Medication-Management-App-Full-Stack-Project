<template>
<!-- Haftalık Durum -->
<div class="card card-sm bg-base-100 shadow-md">
    <div class="card-body">
    <h3 class="text-md font-medium">{{ $t('status.today') }}</h3>
    <progress class="progress progress-primary w-full" :value="stats?.taken_percentage" max="100"></progress>
    <p class="text-sm text-gray-500 mt-1">{{ stats?.taken_count }} / {{ stats?.be_taken_count }} {{ $t('status.dos_taken') }}</p>
    </div>
</div>
</template>

<script setup>
defineProps(['stats'])
</script>