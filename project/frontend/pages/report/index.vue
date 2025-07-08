<template>
<div class="p-4 space-y-4 max-w-md mx-auto">
  <div class="flex flex-col gap-4 flex-1">
    <div class="flex justify-between items-center">
      <h1 class="text-xl font-bold">Raporlarım</h1>
      <button 
        @click="go('/settings')"
        class="btn btn-ghost btn-circle text-2xl p-0">
        <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
      </button>
    </div>
  </div>
  <div class="flex w-full my-2">
    <h2 class="text-lg font-semibold w-full">
      <TodayMessage />
    </h2>
    <button class="btn btn-primary btn-sm" >
      + Yeni Rapor
    </button>
  </div>

  <div>raporlarım</div>
</div>
</template>

<script setup>
const { go } = useLocaleRouter()
</script>