<template>
    <fieldset class="w-full fieldset flex flex-row bg-base-300 rounded-b-lg md:rounded-b-2xl sticky top-0 border-b border-gray-600">
    <div class="flex md:ps-0 min-w-fit">
        <p class="m-auto py-2 px-4 cursor-pointer"
        @click="go('/')"
        >
            <font-awesome :icon="faArrowLeft" />
        </p>
        <h2 class="text-sm md:text-2xl font-mono ps-2 m-auto">İlaç ekleme düzenleme formu</h2>
    </div>
    <div class="w-full"></div>
    <button class="btn btn-sm md:btn-md my-auto me-2 btn-success font-bold text-white" type="button" :disabled="!enable" @click="emit('send')">
        <span class="text-md md:text-lg">Kaydet</span>
    </button>
</fieldset>
</template>

<script setup>
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()

defineProps({
    enable: {
        type: Boolean,
        default: true
    }
})

const emit = defineEmits(['send']);

</script>