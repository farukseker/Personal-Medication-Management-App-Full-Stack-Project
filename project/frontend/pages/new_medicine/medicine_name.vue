<template>
<section class="flex flex-col gap-4">
    <!--fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">Tara</legend>
        
    </fieldset-->
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç bilgileri</legend>
        <div
        class="w-full bg-base-200 "
        :class="on_focus ? 'fixed md:static top-0 left-0 z-10':''"
        >
        <input 
            type="text"
            class="input w-full"
            v-model="new_mdc_store.medicine_name"
            @focusin="on_focus = true"
            @focusout="on_focus = false"
            placeholder="İlaç adı">
            <div v-if="on_focus" class="bg-fuchsia-600 max-h-[20vh]">
                <ul>
                    <li>öneri 1</li>
                    <li>öneri 1</li>
                    <li>öneri 3</li>
                </ul>
            </div>
        </div>
        <article class="flex mt-2 gap-2">
            <input class="input w-2/3" type="number" v-model="new_mdc_store.dose_amount" placeholder="Kullanılacak dos">
            <select v-model="new_mdc_store.dose_unit" class="input w-1/3">
                <option class="text-gray-600" disabled selected>Ölçek</option>
                <option v-for="(dose_unit, index) in new_mdc_store.dose_unit_list" :key="index + 'dose_unit' " class="text-gray-600" :value="dose_unit.param">{{dose_unit.value}}</option>
            </select>
        </article>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">İlaç Notu</legend>
        <textarea v-model="new_mdc_store.medicine_notes" class="input w-full min-h-32"></textarea>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <button class="btn btn-primary" @click="go_next_page">Devam et</button>
    </fieldset>
</section>
</template>

<script setup>
const on_focus = ref(false)
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const new_mdc_store = useNewMdcStore()
const router = useRouter()

const go_next_page = () => {
    new_mdc_store.form_index = 1
    router.push('/new_medicine/medicine_plan')
}

definePageMeta({layout: 'newmdc'})
</script>