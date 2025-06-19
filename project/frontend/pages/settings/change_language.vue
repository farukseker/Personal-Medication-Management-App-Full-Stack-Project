<template>
    <section class="px-4 space-y-4 max-w-md mx-auto">
        <header>
            <button 
             class="btn btn-ghost ps-0 text-xl"
             @click="go('/settings')"
             >
                <font-awesome :icon="faArrowLeft" />
            </button>
            <h1 class="text-xl font-bold">Dil ayarları</h1>
        </header>
        <article>
            <fieldset class="w-full fieldset shadow rounded-box p-2">
                <legend class="fieldset-legend font-bold">Dil Seçiniz</legend>
                <label class="input w-full">
                    <font-awesome :icon="faSearch" />
                    <input type="text" class="grow" v-model="search" placeholder="Dil ara...">
                </label>
                <NuxtLink
                    v-for="lang in filteredLocales"
                    :key="locale.code"
                    class="btn"
                    :class="lang.code === locale ? 'btn-primary':' btn-ghost'"
                    :to="switchLocalePath(lang.code)"
                >
                    <span :class="`fi fi-${lang.code}`"></span>
                    <span class="text-start w-full">{{ lang.name }}</span>
                </NuxtLink>
            </fieldset>
        </article>
    </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { faArrowLeft, faSearch } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const search = ref('')

const availableLocales = computed(() => locales.value)

const filteredLocales = computed(() => {
  return availableLocales.value.filter(lang => 
    lang.name.toLowerCase().includes(search.value.toLowerCase()) || 
    lang.code.toLowerCase().includes(search.value.toLowerCase())
  )
})
</script>