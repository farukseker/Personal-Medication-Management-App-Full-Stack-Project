<template>
  <section>
    <div class="space-y-3 max-h-[40vh] overflow-y-auto py-4">
      <MedicationPillReminder
        v-if="medication_today_list.length > 0"
        v-for="medication_today in medication_today_list"
        :key="medication_today.id" 
        :medication="medication_today" 
        @load_medication="async () => await load_medication_today_list()" />
      <AlertsTakedAllPills v-else-if="stats?.taken_percentage == 100" />
      <AlertsPillsNotfound v-else />
    </div>
    <StatusWeeklyStatus :stats="stats" />
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const medication_today_list = ref([])
const stats = ref(null)

async function load_medication_today_list() {
  // API veya store çağrısı
}

onMounted(() => {
  load_medication_today_list()
})
</script>
