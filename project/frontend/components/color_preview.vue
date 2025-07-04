<template>

<div class="font-semibold flex w-full bg-transparent" :data-theme="theme">
    <div class="w-1.5 bg-base-300" style=" border-start-start-radius: 16px; border-end-start-radius: 16px"></div>
    <div class="bg-base-100 hover:bg-base-200 w-full p-2">
    <span>{{ theme }}</span>
    <ul class="flex gap-2">
        <li class="w-5 h-5 flex text-sm bg-primary text-primary-content border justify-center">A</li>
        <li class="w-5 h-5 flex text-sm bg-secondary text-secondary-content border justify-center">A</li>
        <li class="w-5 h-5 flex text-sm bg-accent text-accent-content border justify-center">A</li>
        <li class="w-5 h-5 flex text-sm bg-neutral text-neutral-content border justify-center">A</li>
        <li class="w-5 h-5 bg-primary-content btn btn-primary"></li>
        <li class="w-5 h-5 bg-secondary-content rounded-2xl border border-dashed"></li>
    </ul>
    </div>
</div>

</template>

<script setup>
defineProps({
    theme: {
        type: String,
        required: true
    }
})
</script>