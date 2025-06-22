<template>
<section class="px-4 space-y-4 max-w-md mx-auto">
    <header>
        <button class="btn btn-ghost ps-0 text-xl">
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold">Bildirim ayarları</h1>
    </header>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold text-lg">İlaç hatırlatıcısı</legend>
            <p class="text-lg font-semibold font-sans text-pretty">
                Sabah <span class="text-primary">08:30</span> dan akşam <span class="text-primary">10:30</span> 'a kadar bildirim alıcaksınız
            </p>
            <hr>
            <fieldset class="fieldset">
                <legend class="fieldset-legend">What is your name?</legend>
                <label class="input w-full">
                    <span class="w-4 h-4 m-auto">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M464 256A208 208 0 1 1 48 256a208 208 0 1 1 416 0zM0 256a256 256 0 1 0 512 0A256 256 0 1 0 0 256zM232 120l0 136c0 8 4 15.5 10.7 20l96 64c11 7.4 25.9 4.4 33.3-6.7s4.4-25.9-6.7-33.3L280 243.2 280 120c0-13.3-10.7-24-24-24s-24 10.7-24 24z"/></svg>
                    </span>
                    <input class="grow" type="time">
                </label>
                <p class="label">Optional</p>
            </fieldset>
        </fieldset>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold text-lg">Su hatırlatıcısı</legend>
        </fieldset>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold text-lg">Kilo takibi hatırlatıcısı</legend>
        </fieldset>
    </article>
</section>
</template>
<script setup>
import { 
    faArrowLeft,
    faClock,
    faClockFour,
    faClockRotateLeft
 } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
</script>