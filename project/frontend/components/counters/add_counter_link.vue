<template>
<!-- Add a counter -->
<div 
    @click="go('/new_counter')"
    class="rounded shadow-md bg-base-200 border-2 border-dashed border-gray-400 text-gray-600 p-2 flex cursor-pointer">
    <span class="my-auto">{{ $t('counter.add_counter') }}</span>
</div>
</template>

<script setup>
import { useLocaleRouter } from '~/composables/useLocaleRouter'
const { go } = useLocaleRouter()
</script>