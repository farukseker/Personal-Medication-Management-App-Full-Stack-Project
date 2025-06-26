<template>
  <section class="px-4 space-y-4 max-w-md mx-auto">
    <header class="flex">
      <button class="btn btn-ghost ps-0 text-xl" @click="go('/tab/water_tracking')">
        <font-awesome :icon="faArrowLeft" />
      </button>
      <h1 class="text-xl font-bold w-full text-center my-auto -ms-4">Yeni hedef belirle</h1>
    </header>

    <article class="space-y-4">
      <!-- Kilo Girişi -->
      <div>
        <label class="block mb-1 font-semibold">Kilonuz (kg)</label>
        <input type="number" v-model.number="weight" class="input input-bordered w-full" />
      </div>

      <!-- Hesapla Butonu -->
      <button class="btn btn-primary w-full" @click="handleCalculate">Günlük ihtiyacı hesapla</button>

      <!-- Hedef Girişi -->
      <div>
        <label class="block mb-1 font-semibold">Günlük hedefiniz (litre)</label>
        <input ref="targetInput" type="number" v-model.number="target" class="input input-bordered w-full" />
      </div>

      <!-- Kaydet Butonu -->
      <button class="btn btn-success w-full" @click="saveTarget">Kaydet</button>
    </article>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()

const weight = ref(null)
const target = ref(null)
const targetInput = ref(null)

function getSeason(date = new Date()) {
  const month = date.getMonth() + 1
  if ([12, 1, 2].includes(month)) return 'winter'
  if ([3, 4, 5].includes(month)) return 'spring'
  if ([6, 7, 8].includes(month)) return 'summer'
  return 'autumn'
}

function calculateWaterIntake(weight) {
  const season = getSeason()
  let base = weight * 0.033
  if (season === 'summer') base += 0.5
  if (season === 'winter') base -= 0.2
  return parseFloat(base.toFixed(2))
}

function handleCalculate() {
  if (!weight.value) return alert('Lütfen kilonuzu girin')
  target.value = calculateWaterIntake(weight.value)
  targetInput.value?.focus()
}

async function saveTarget() {
  if (!target.value) {
    alert('Lütfen bir hedef belirleyin')
    return
  }

  try {
    const res = await fetch('/api/water_target/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Authorization token gerekiyorsa buraya ekle
      },
      body: JSON.stringify({
        daily_target_liters: target.value
      })
    })

    if (!res.ok) throw new Error('API isteği başarısız')

    alert('Hedef başarıyla kaydedildi!')
    go('/tab/water_tracking')
  } catch (e) {
    console.error(e)
    alert('Bir hata oluştu.')
  }
}
</script>
