<template>
  <div class="max-w-md mx-auto">
    <button @click="show = true">Aç</button>

    <VueFinalModal v-model="show"
      :transition="'fade'"
      :overlay-transition="'fade'"
      class="max-w-md mx-auto"
    >
      <div class="p-4 bg-white rounded">Modal İçeriği</div>
    </VueFinalModal>
  </div>
</template>

<script setup>
import { VueFinalModal } from 'vue-final-modal'
const show = ref(false)
</script>
