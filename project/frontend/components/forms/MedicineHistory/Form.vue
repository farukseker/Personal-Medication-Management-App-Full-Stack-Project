<template>
    <!-- Open the modal using ID.showModal() method -->
    <!-- Open Modal Button -->
<button class="btn btn-primary w-full sm:w-auto" onclick="my_modal_2.showModal()">İlaç Seç</button>

<!-- Modal -->
<dialog id="my_modal_2" class="modal">
  <div class="modal-box bg-base-300 flex flex-col gap-6 p-6 rounded-2xl max-w-md w-full mx-auto">
    
    <!-- İlaç Seçimi -->
    <fieldset class="flex flex-col gap-2">
      <legend class="text-lg font-semibold">İlaç Seç</legend>
      <select 
        v-model="sleected_medicine"
        class="select select-bordered w-full"
        @change="used_dosage = $event.target.value.dosage"
      >
        <option disabled selected>İlaç seçin</option>
        <option
          :value="next_medication"
          v-for="next_medication in my_medication_store.nextMedicationList"
        >
          {{ next_medication.medication_name }}
        </option>
      </select>
    </fieldset>

    <!-- Dozaj Ayarı -->
    <fieldset v-if="sleected_medicine" class="flex flex-col gap-3">
      <template v-if="sleected_medicine.scheduled_time">
        <legend class="text-lg font-semibold">Planlanan Saat</legend>
        <p>
          <font-awesome :icon="faClockFour" />
        {{ sleected_medicine.scheduled_time }}
        </p>
        <p>
          Bugün {{ sleected_medicine.taken_count }} Kez aldın,
          <br>
          Bugün {{ sleected_medicine.reminder_total }} kere alacaksın
        </p>
      </template>
      
      <legend class="text-lg font-semibold">Dozaj</legend>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <input
          type="number"
          class="input input-bordered w-full text-center sm:col-span-2"
          v-model="used_dosage"
        />
        <button
          class="btn btn-secondary text-white text-sm font-bold w-full"
          @click="used_dosage = sleected_medicine.dosage"
        >
          {{ sleected_medicine.dosage }} {{ sleected_medicine.dosage_type }}
        </button>
      </div>
    </fieldset>

    <!-- Kullan Butonu -->
    <fieldset>
      <form method="dialog" class="modal-backdrop">
        <button class="btn btn-success w-full text-white text-lg" @click="use_a_medication">Kullan</button>
      </form>
    </fieldset>
  </div>

  <!-- Arka Plan Tıklama ile Kapat -->
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
</template>

<script setup>
const { $api } = useNuxtApp()
import { faClockFour } from '@fortawesome/free-solid-svg-icons'
import { useMyMedicationStore } from '@/stores/my_medication_store.js'
const my_medication_store = useMyMedicationStore()

const sleected_medicine = ref()
const used_dosage = ref('')

const load_next_medicine_names = async () => {
  await my_medication_store.getNextMedicationList()
  await my_medication_store.getMyMedicationList()
}

onMounted(load_next_medicine_names)
onBeforeMount(load_next_medicine_names)

const use_a_medication = async () => {
  if (sleected_medicine.value === null){return;}
  await my_medication_store.addUsedMedication({
    dosage: used_dosage.value,
    medication: sleected_medicine.value.medication_id
  })
  sleected_medicine.value = null
}

</script>