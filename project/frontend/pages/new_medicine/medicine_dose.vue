<template>
<section class="flex flex-col gap-4">
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <legend class="fieldset-legend font-bold">
            Haftalık Doz planı (Opsiyonel)
        </legend>
        <article class="flex mb-2 gap-2">
            <strong class="my-auto text-lg">1.</strong>
            <input class="input w-2/3" type="text" placeholder="Miktar">
            <select class="input w-1/3">
                <option class="text-gray-600" disabled selected>Ölçek</option>
                <option class="text-gray-600" value="">x</option>
            </select>
        </article>
        <button class="btn btn-secondary">Hafta Ekle</button>
    </fieldset>
    <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
        <div class="flex gap-2 w-full">
            <div class="w-full">
                <button class="btn btn-secondary w-full">Geri</button>
            </div>
            <div class="w-full">
                <button class="btn btn-primary w-full">Devam et</button>
            </div>
        </div>
    </fieldset>
</section>
</template>

<script setup>
const on_focus = ref(false)
//new_medicine_form_layout/
definePageMeta({layout: 'newmdc'})
</script>