<template>
  <nav class="tabs tabs-lift tabs-md tabs-top">
    <button @click="go('/')" class="tab hover:text-primary flex gap-2" :class="isPathEqual('/') ? 'tab-active': ''">
      <font-awesome :icon="faPills" /> {{ $t('index.medications') }}
    </button>
    <button @click="go('/tab/counters')" class="tab hover:text-primary flex gap-2" :class="isPathEqual('/tab/counters') ? 'tab-active': ''">
      <font-awesome :icon="faPlus" /> {{ $t('index.counter') }}
    </button>
    <button @click="go('/tab/water_tracking')" class="tab hover:text-primary flex gap-2" :class="isPathEqual('/tab/water_tracking') ? 'tab-active': ''">
      <font-awesome :icon="faGlassWater" /> {{ $t('index.water_tracking') }}
    </button>
    <button @click="go('/tab/weight_tracking')" class="tab hover:text-primary flex gap-2" :class="isPathEqual('/tab/weight_tracking') ? 'tab-active': ''">
      <font-awesome :icon="faWeightScale" /> {{ $t('index.weight_tracking') }}
    </button>
  </nav>
</template>

<script setup>
import { faPills, faPlus, faGlassWater, faWeightScale } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
const route = useRoute()
const localePath = useLocalePath()
const isPathEqual = (path) => route.path === localePath(path) 
</script>