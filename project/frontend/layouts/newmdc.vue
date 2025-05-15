<template>
<div class="p-4 space-y-4 max-w-md mx-auto">
    <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takip Formu</h1>
            <button class="btn btn-ghost text-2xl">
                pp
            </button>
        </div>
    </div>
    <div> 
        <div class="flex w-full">
          <h2 class="text-lg font-semibold mb-2 w-full">İlaç Ekle/Düzenle</h2>
        </div>
        {{ new_mdc_store.form_index }}
        <ul class="steps">
            <li
            class="step"
            :class="new_mdc_store.form_index >= 0 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faPills" />
                </span>
                Register
            </li>
            <li 
            class="step"
            :class="new_mdc_store.form_index >= 1 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faCalendar" />
                </span>
            Choose plan
            </li>
            <li class="step"
            :class="new_mdc_store.form_index >= 2 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faClock" />
                </span>
                Purchase
            </li>
            <li class="step"
            :class="new_mdc_store.form_index >= 3 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faClock" />
                </span>
                Receive Product
            </li>
        </ul>
        <ul>
            <li @click="$router.push('/new_medicine/medicine_name')">
                medicine name
            </li>
            <li @click="$router.push('/new_medicine/medicine_plan')">
                medicine plan
            </li>
            <li @click="$router.push('/new_medicine/medicine_clock')">
                medicine clock
            </li>
            <li @click="$router.push('/new_medicine/medicine_dose')">
                medicine dose
            </li>
        </ul>
        <slot />
    </div>
</div>
</template>

<script setup>
import { faTablets, faPills, faPlus, faClock, faCalendar, faHome, faBucket } from '@fortawesome/free-solid-svg-icons'
import { useNewMdcStore } from '@/stores/new_mdc_store.js'

const new_mdc_store = useNewMdcStore()
onMounted(() => {
    const theme = localStorage.getItem('theme') || 'light'
    document.documentElement.setAttribute('data-theme', theme)
})
</script>