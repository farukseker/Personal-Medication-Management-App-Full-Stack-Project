<template>
<div class="flex flex-col gap-4 items-center px-8">
    <div class="flex w-full ">
      <button class="btn btn-ghost">🎯 Yeni hedef belirle</button>
      <button class="btn btn-ghost">🔔 Hatırlatıcı ayarları</button>
    </div>
    
    <div class="space-y-4 py-4 grid grid-cols-2 gap-4">
      <div class="radial-progress text-blue-400 scale-150 text-xl" :style="`--value:${progress};`" :aria-valuenow="progress" role="progressbar">
        <span class="text-lg">{{ total }} ml</span>
      </div>
      <div>
        <ul>
          <li><span class="font-semibold">Hedef</span>: {{goal}} ml</li>
          <li><span class="font-semibold">Ulaşılan</span>: {{ total }} ml</li>
        </ul>
      </div>
    </div>

    <div class="grid grid-cols-2 gap-4 w-full">
      <div
        class="water-button"
        @click="input=100;addWater()"
        >
        <font-awesome :icon="faDroplet" class="my-auto text-xl" />
        <span class="text-lg font-bold text-center">100ml</span>
      </div>
      <div 
        class="water-button"
        @click="input=250;addWater()"
      >
        <font-awesome :icon="faGlassWater" class="my-auto text-xl" />
        <span class="text-lg font-bold text-center">250ml</span>
      </div>
      <div 
        class="water-button"
        @click="input=300;addWater()"
      >
        <font-awesome :icon="faMugSaucer" class="my-auto text-xl" />
        <span class="text-lg font-bold text-center">400ml</span>
      </div>
      <div 
        class="water-button"
        @click="input=400;addWater()"
      >
        <font-awesome :icon="faBucket" class="my-auto text-xl" />
        <span class="text-lg font-bold text-center">400 ml</span>
      </div>
    </div>

    <div class="w-full flex flex-col gap-2" name="water nav">
      <ul class="flex flex-col gap-2">
        <li class="w-full bg-blue-50 p-2 rounded grid grid-cols-5" v-for="hst in history">
          <div class="col-span-2 flex">
            <font-awesome :icon="getIconFromAmount(hst.amount)" class="my-auto text-xl" />
            <span class="my-auto">{{ hst.amount }}</span>
          </div>
          <div class="col-span-2 flex">
            <span class="my-auto">{{ hst.time }}</span>
          </div>
          <button class="col-span-1 btn btn-sm btn-error ">
            <font-awesome :icon="faX" />
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>
<style>
.water-button{
  @apply btn btn-ghost flex p-4 min-h-20 max-h-20 flex-col justify-center border rounded-lg text-blue-800 bg-blue-200 shadow cursor-pointer 
}
</style>
<script setup>
// ------ su 
import { faBucket, faGlassWater, faDroplet, faMugSaucer, faX } from '@fortawesome/free-solid-svg-icons'

const goal = 2000 // Günlük hedef (ml)
const total = ref(0)
const input = ref(null)
const history = ref([])

const getIconFromAmount = (amount) => {
  switch (amount){
    case 100:
      return faDroplet
    case 250:
      return faGlassWater
    case 300:
      return faMugSaucer
    case 400:
      return faBucket
  }
}

const addWater = () => {
  if (!input.value || input.value <= 0) return

  total.value += input.value
  history.value.unshift({
    amount: input.value,
    time: new Date().toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' }),
  })
  input.value = null
}

const progress = computed(() => Math.min(Math.round((total.value / goal) * 100), 100))
</script>