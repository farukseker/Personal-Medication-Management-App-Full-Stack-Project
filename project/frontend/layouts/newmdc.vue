<template>
<div class="py-4 px-2 sm:px-4 space-y-4 max-w-md mx-auto">
    <div class="flex flex-col gap-4 flex-1">
        <div class="flex justify-between items-center">
            <h1 class="text-xl font-bold">İlaç Takip Formu</h1>
            <button 
              @click="$router.push('/settings')"
              class="btn btn-ghost text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
            </button>
        </div>
    </div>
    <div class="pb-14"> 
        <div class="flex w-full shadow-sm rounded">
            <div class="radial-progress progress-primary" style="--value:35;" aria-valuenow="2" role="progressbar">
              3 / 1
            </div>
            <div class="w-fit ms-4 mt-2 text-xl font-semibold">
              <p>
                İlaç Düzenle
                <span class="label block w-full text-sm">Sonraki adım: planlama</span>
              </p>
            </div>
        </div>

        <!--ul class="steps mx-auto w-full">
            <li
            @click="$router.push('/new_medicine/medicine_name'); new_mdc_store.form_index = 0"
            class="step"
            :class="new_mdc_store.form_index >= 0 ? 'step-primary': ''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faPills" />
                </span>
            </li>
            <li 
            @click="$router.push('/new_medicine/medicine_plan'); new_mdc_store.form_index = 1"
            class="step"
            :class="new_mdc_store.form_index >= 1 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faCalendar" />
                </span>
            </li>
            <li 
            @click="$router.push('/new_medicine/medicine_clock'); new_mdc_store.form_index = 2"
            class="step"
            :class="new_mdc_store.form_index >= 2 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faClock" />
                </span>
            </li>
            <li 
            @click="$router.push('/new_medicine/medicine_dose'); new_mdc_store.form_index = 3"
            class="step"
            :class="new_mdc_store.form_index >= 3 ? 'step-primary':''"
            >
                <span class="step-icon">
                    <font-awesome :icon="faClock" />
                </span>
            </li>
        </ul-->
        <div class="relative overflow-hidden py-4 sm:p-4 space-y-4 max-w-md mx-auto">
            <transition
            :name="transitionName"
            mode="out-in"
            >
                <slot />
            </transition>
        </div>
    </div>
    <NavBottomNav />

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

const transitionName = ref('slide-left')
let previousIndex = ref(new_mdc_store.form_index)

watch(() => new_mdc_store.form_index, (newVal, oldVal) => {
  transitionName.value = newVal > oldVal ? 'slide-left' : 'slide-right'
  previousIndex.value = newVal
})
</script>

<style scoped>
.slide-left-enter-active,
.slide-right-enter-active {
  @apply transition-all duration-300 ease-in-out;
}

.slide-left-leave-active,
.slide-right-leave-active {
  @apply transition-all duration-300 ease-in-out;
}

.slide-left-enter-from {
  @apply translate-x-full opacity-0;
}
.slide-left-enter-to {
  @apply translate-x-0 opacity-100;
}
.slide-left-leave-from {
  @apply translate-x-0 opacity-100;
}
.slide-left-leave-to {
  @apply -translate-x-full opacity-0;
}

.slide-right-enter-from {
  @apply -translate-x-full opacity-0;
}
.slide-right-enter-to {
  @apply translate-x-0 opacity-100;
}
.slide-right-leave-from {
  @apply translate-x-0 opacity-100;
}
.slide-right-leave-to {
  @apply translate-x-full opacity-0;
}

</style>