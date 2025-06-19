<template>
<section class="px-4 space-y-4 max-w-md mx-auto">
    <header>
        <button class="btn btn-ghost ps-0 text-xl">
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold">Ayarlar</h1>
    </header>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold">Kullanıcı ayarları</legend>
            <SettingsButton :icon="faUser" title="pars" to="/" />
            <SettingsButton :icon="faUser" title="Kişisel bilgiler" to="/" />
            <SettingsButton :icon="faKey" title="Şifre değiştir" to="/" />
        </fieldset>
    </article>
    <article>
        <fieldset class="w-full fieldset shadow rounded-box p-2">
            <legend class="fieldset-legend font-bold">Destek ve Hakkında</legend>
            <SettingsButton :icon="faHeadset" title="Destek" to="/" />
            <SettingsButton :icon="faScroll" title="Hakkında" to="/" />
        </fieldset>
    </article>
    <p class="text-gray-400 text-sm text-center">Version. PARS | V1.12.8 - f4rukseker</p>
</section>
</template>

<script setup>
import { 
    faHeadset,
    faArrowLeft,
    faUser,
    faKey,
    faScroll,
 } from '@fortawesome/free-solid-svg-icons'

</script>