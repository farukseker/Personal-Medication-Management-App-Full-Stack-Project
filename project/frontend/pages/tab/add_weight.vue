<template>
    <section class="px-4 space-y-4 max-w-md mx-auto">
    <header>
        <button 
            class="btn btn-ghost ps-0 text-xl py-2"
            @click="go('/tab/weight_tracking')"
            >
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold">Kilo ekle</h1>
    </header>
    <form>

    <article class="flex flex-col gap-4">
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold text-lg text-pretty text-primary">Kilo bilgilerinizi giriniz</legend>
            <label class="input w-full">
                <font-awesome :icon="faCalendar" />
                <input type="date" class="grow" placeholder="Tarih">
            </label>
            <label class="input w-full">
                <font-awesome :icon="faWeight" />
                <input type="number" class="grow" placeholder="Kilo">
            </label>

        </fieldset>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <div class="grid grid-cols-2 gap-2">
                <button type="button" @click="go('/tab/weight_tracking')" class="btn btn-secondary">Geri</button>
                <button type="submit" class="btn btn-primary">Ekle</button>
            </div>
        </fieldset>
    </article>
    
    </form>

    </section>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
import { 
    faCalendar,
    faWeight,
    faArrowLeft,
 } from '@fortawesome/free-solid-svg-icons'

</script>