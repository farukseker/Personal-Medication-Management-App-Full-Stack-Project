<template>
    <div class="dock max-w-md mx-auto">
      <button
      @click="$router.push('/')"
    :class="$route.path === '/' ? 'dock-active':''"
      >
        <font-awesome :icon="faHome" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.home') }}</span>
      </button>

      <button 
        @click="$router.push('/history')"
        :class="$route.path === '/history' ? 'dock-active':''"
        >
        <font-awesome :icon="faCalendar" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.history') }}</span>
      </button>
      
      <button
        @click="$router.push('/medications')"
        :class="$route.path === '/medications' ? 'dock-active':''"
        >
        <font-awesome :icon="faPills" class="size-[1.2em]" />
        <span class="dock-label">{{ $t('bottom_navigation.medications') }}</span>
      </button>

      <button
        @click="$router.push('/settings')"
        :class="$route.path === '/settings' ? 'dock-active':''"
        >
        <font-awesome :icon="faGear" />
        <span class="dock-label">{{ $t('bottom_navigation.settings') }}</span>
      </button>
    </div>
</template>
<script setup>
import { faPills, faGear, faCalendar, faHome } from '@fortawesome/free-solid-svg-icons'
</script>