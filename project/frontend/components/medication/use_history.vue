<template>
  <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">
    <h2>Aldığım ilaçlar</h2>
  </legend>
      <!--TransitionGroup name="slide-fade" tag="ul" class="w-full flex flex-col gap-2"-->
      <ul v-if="my_medication_store.medicationList.length > 0" class="w-full flex flex-col gap-2">
        <li class="grid grid-cols-6 bg-base-100 py-2 rounded shadow-sm border-b "
          v-for="(medication_history, index) in my_medication_store.medicationList"
          :key="medication_history.id"
          >
          <div class="p-2 bg-base-100 rounded-full flex-shrink-0 m-auto">
              <font-awesome :icon="faPills" />
          </div>
          <div class="col-span-4">
            <div class="flex">
              <div class="w-full flex flex-col">
                <strong class="text-sm">{{ medication_history.medication_name }}</strong>
                <p class="text-xs">{{ medication_history.use_date }} {{ medication_history.use_time.slice(0, 5) }}</p>
              </div>
              <div class="w-1/4 text-xs flex">
                <p class="mx-auto mt-1 flex flex-col text-center">
                  <strong class="font-semibold text-lg">{{ medication_history.dosage }}</strong>
                  <span>{{ medication_history.dosage_type }}</span>  
                </p>
              </div>
            </div>
          </div>
          <div class="flex m-auto w-full px-2">
            <button 
              class="btn btn-error btn-sm md:btn-md w-full"
              @click="deleteMedication(index)"
              >Sil</button>
          </div>
        </li>
      </ul>
      <strong v-else>Henüz bir ilaç almadın</strong>

      <!--/TransitionGroup-->
  </fieldset>
</template>

<script setup>
import { faHome, faPills, faPlus, faTrash, faEnvelope, faHandFist, faUserGroup } from '@fortawesome/free-solid-svg-icons'

import { useMyMedicationStore } from '@/stores/my_medication_store.js'
const my_medication_store = useMyMedicationStore()

onMounted(my_medication_store.getMedicationList)

const swipedIndex = ref(null)
const swipedToDeleteIndex = ref(null)
const swipeOffsets = reactive({})

let startX = 0

function startTouch(e, index) {
  startX = e.touches[0].clientX
  swipedIndex.value = index
}

function moveTouch(e, index) {
  const currentX = e.touches[0].clientX
  let offset = currentX - startX

  // sadece sola kaydırmaya izin ver
  if (offset < 0) {
    swipeOffsets[index] = Math.max(offset, -180) // max -80px
  } else {
    swipeOffsets[index] = 0
  }
}

function endTouch(index) {
  if (Math.abs(swipeOffsets[index]) < 40) {
    // az kaydırdıysa geri al
    swipeOffsets[index] = 0
      swipedIndex.value = null
     swipedToDeleteIndex.value = null
  } else {
    // yeterince kaydırdıysa kilitle
    swipeOffsets[index] = -180
    swipedToDeleteIndex.value = index
    deleteMedication(index)
    }
}

async function deleteMedication(index) {
  await my_medication_store.deleteMedicationObjFromIndex(index)
  delete swipeOffsets[index]
  swipedIndex.value = null
  swipedToDeleteIndex.value = null
}
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(-20px);
  opacity: 0;
}
</style>