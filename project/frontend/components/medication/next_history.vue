<template>
  <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">
    <h2>İlaçlar</h2>
  </legend>
      <!--TransitionGroup name="slide-fade" tag="ul" class="w-full flex flex-col gap-2"-->
      <ul class="w-full flex flex-col gap-2">
        <li class="grid grid-cols-6 py-2 rounded shadow bg-base-100 border-b"
          v-for="(medication_history, index) in my_medication_store.nextMedicationList"
          :key="medication_history.id"
          >
          <div class="p-2 bg-base-100 rounded-full flex-shrink-0 m-auto">
              <font-awesome :icon="faPills" />
          </div>
          <div class="col-span-4">
            <div class="flex">
              <div class="w-full flex flex-col">
                <strong class="text-sm">{{medication_history.medication_name}}</strong>
                <p class="text-xs">{{ medication_history.scheduled_time ? medication_history.scheduled_time.slice(0, 5) : 'Plansız'  }}</p>
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
              class="btn btn-primary btn-sm md:btn-md w-full"
              @click="deleteMedication(index)"
              >Ekle</button>
          </div>
        </li>
      </ul>
      <!--/TransitionGroup-->
  </fieldset>
</template>

<script setup>
import { faPills, faPlus } from '@fortawesome/free-solid-svg-icons'
import { useMyMedicationStore } from '@/stores/my_medication_store.js'


const my_medication_store = useMyMedicationStore()
onMounted(my_medication_store.getNextMedicationList)

const swipedIndex = ref(null)
const swipedToUseIndex = ref(null)
const swipeOffsets = reactive({})

let startX = 0
let startY = 0;

function startTouch(e, index) {
  const touch = e.touches[0];
  startX = touch.clientX;
  startY = touch.clientY;
  swipedIndex.value = index
}

function moveTouch(e, index) {
  // const currentX = e.touches[0].clientX
  const touch = e.touches[0];
  const deltaX = touch.clientX - startX;
  const deltaY = touch.clientY - startY;

  let offset = deltaX - startX

  if (Math.abs(deltaX) > Math.abs(deltaY)) {
    e.preventDefault();
    if (offset < 0) {
      swipeOffsets[index] = Math.max(offset, -180) // max -80px
    } else {
      swipeOffsets[index] = 0
    }
  } else {
    
  }

}

function endTouch(index) {
  if (Math.abs(swipeOffsets[index]) < 40) {
    // az kaydırdıysa geri al
    swipeOffsets[index] = 0
      swipedIndex.value = null
     swipedToUseIndex.value = null
  } else {
    // yeterince kaydırdıysa kilitle
    swipeOffsets[index] = -180
    swipedToUseIndex.value = index
    deleteMedication(index)
    }
}

async function deleteMedication(index) {
  const next_medication = my_medication_store.nextMedicationList[index]
  await my_medication_store.addUsedMedication({
    dosage: next_medication.dosage,
    medication: next_medication.medication_id
  })
  delete swipeOffsets[index]
  swipedIndex.value = null
  swipedToUseIndex.value = null
}


</script>

<style scoped>
.touch-item {
  /* sadece dikey kaydırmayı tarayıcıya bırak */
  touch-action: pan-y;
}

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