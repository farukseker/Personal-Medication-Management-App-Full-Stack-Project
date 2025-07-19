<template>
   <div class="p-4 space-y-4 max-w-md mx-auto">
        <form @submit.prevent="" class="bg-base-100 my-3">
            <fieldset class="fieldset">
                <legend class="fieldset-legend">Filitre başlangıç tarihi ?</legend>
                <label class="input w-full">
                    <font-awesome :icon="faCalendarDay" />
                    <input class="grow" type="text">
                </label>
            </fieldset>
            <fieldset class="fieldset">
                <legend class="fieldset-legend">Filitre bitiş tarihi ? <span class="text-secondary-content">(opsiyanel)</span></legend>
                <label class="input w-full">
                    <font-awesome :icon="faCalendarDay" />
                    <input class="grow" type="text">
                </label>
            </fieldset>
            <div class="w-full text-end mt-2">
                <button class="btn btn-primary">Filitrele</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { 
    faCalendarDay
} from '@fortawesome/free-solid-svg-icons'
</script>