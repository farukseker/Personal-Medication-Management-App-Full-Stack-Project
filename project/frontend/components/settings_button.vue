<template>
    <button
        :class="btnStyle"
        @click="goTo"
    >
        <font-awesome :icon="icon" class="my-auto" /> 
        <p class="w-full text-start ps-1 my-auto">{{ title }}</p>
        <p class="text-secondary" v-if="description">{{ description }}</p>
        <font-awesome v-if="showEndArrow" :icon="faAngleRight" class="my-auto" /> 
    </button>
</template>

<script setup>
import { faAngleRight } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
const { to } = defineProps({
    btnStyle: {
        type: String,
        required: false,
        default: 'btn btn-ghost'    
    },
    to: {
        type: String,
        required: true,
    },
    icon: {
        required: false,
    },
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: false,
    },
    showEndArrow:{
        type: Boolean,
        required: false,  
        default: true    
    }
})

const goTo = () => {
    go(to)   
}
</script>