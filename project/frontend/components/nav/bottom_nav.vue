<template>
    <div class="dock max-w-md mx-auto">
      <button
        @click="go('/')"
        :class="isPathEqual('/') ? 'dock-active':''"
      >
        <font-awesome :icon="faHome" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.home') }}</span>
      </button>

      <button 
        @click="go('/history')"
        :class="isPathEqual('history') ? 'dock-active':''"
      >
        <font-awesome :icon="faCalendar" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.history') }}</span>
      </button>
      
      <button
        @click="go('/medications')"
        :class="isPathEqual('medications') ? 'dock-active':''"
      >
        <font-awesome :icon="faPills" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.medications') }}</span>
      </button>

      <button
        @click="go('/settings')"
        :class="isPathEqual('settings') ? 'dock-active':''"
      >
        <font-awesome :icon="faGear" />
        <span class="dock-label">{{ $t('bottom_navigation.settings') }}</span>
      </button>
    </div>
</template>
<script setup>
import { faPills, faGear, faCalendar, faHome } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()

const localePath = useLocalePath()
const route = useRoute()
const isPathEqual = (path) => route.path === localePath(path) 
</script>