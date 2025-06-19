<template>
<div class="p-4 space-y-4 max-w-md mx-auto">
    <div class="flex flex-col gap-4 flex-1">
    <div class="flex justify-between items-center">
        <button 
            @click="go('/tab/counters')"
            class="btn btn-ghost max-w-fit text-xl"
        >
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold w-full">Yeni Sayaç Ekle</h1>
        <button 
            @click="go('/settings')"
            class="btn btn-ghost btn-circle text-2xl p-0">
            <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
        </button>
        </div>
    </div>
    <form @submit.prevent="save_new_counter">
        <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4">
            <legend class="fieldset-legend font-bold">İlaç bilgileri</legend>
                <label>Sayaç Adı</label>
                <input type="text" v-model="name" class="input w-full" placeholder="Sayaç adı">
                <label>Sayım şekili</label>
                <input type="text" v-model="unit" class="input w-full" placeholder="Tane, Kez, Defa, Kere, .">
                <button class="btn btn-primary w-full mt-2" :disabled="!name.length > 0">Oluştur</button>
        </fieldset>
    </form>
</div>
</template>

<script setup>
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()

const { $api } = useNuxtApp()
const router = useRouter()

const name = ref('')
const unit = ref('')

const save_new_counter = async () => {
    await $api('/counter/', {
        method: 'POST',
        body: {
            name: name.value,
            unit: unit.value
        }
    })
    go('/')
}
</script>