<template>
  <article class="w-full my-4">
    <div class="flex">
      <input
        type="checkbox"
        class="my-auto checkbox checkbox-success"
        id="use_reminder"
        v-model="use_reminder"
      />
      <label class="label" for="use_reminder">Hatırlatıcı kullan</label>
    </div>

    <div v-if="use_reminder" class="mt-2">
      <div class="flex gap-2">
        <input type="time" v-model="newTime" class="input input-sm md:input-md w-full" placeholder="Saat giriniz"/>
        <button class="btn btn-sm md:btn-md btn-success text-white disabled:text-gray-200" @click="addTime" :disabled="!newTime">
          <span class="text-base dark:text-white">Ekle</span>
        </button>
      </div>

      <ul class="mt-4 space-y-2">
        <li
          v-for="(time, index) in sortedTimes"
          :key="index"
          class="flex justify-between items-center"
        >
          <span>{{ time }}</span>
          <button class="btn btn-sm btn-error" @click="removeTime(index)">
            <span class="text-white">
                Sil
            </span>
          </button>
        </li>
      </ul>
    </div>
  </article>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'
const medicine_store = useMedicineFormStore()

const use_reminder = ref(true)
const newTime = ref('')

const times = computed({
  get: () => medicine_store.remind_times,
  set: (val) => {
    medicine_store.remind_times = val
  }
})

const addTime = () => {
  medicine_store.addRemindTime(newTime.value)
  newTime.value = ''
}

const removeTime = (index) => {
  medicine_store.removeRemindTime(index)
}

// Otomatik sıralama
const sortedTimes = computed(() =>  times.value ?  [...times.value].sort((a, b) => (a > b ? 1 : -1)) : [])
</script>
