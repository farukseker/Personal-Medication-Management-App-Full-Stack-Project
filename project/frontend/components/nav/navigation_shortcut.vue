<template>
    <div class="z-10 fixed bottom-20 right-0 w-[200px] h-[200px] grid grid-cols-2 grid-rows-2 pointer-events-none">
      <div class="w-full h-full flex justify-center relative">
        <Transition>
          <button 
          v-if="show_shurtcuts" 
          class="btn btn-circle btn-success text-white text-lg mt-auto ms-auto shadow pointer-events-auto">
            <font-awesome :icon="faPills" />
          </button>
        </Transition>
      </div>
      <div class="w-full h-full flex justify-center">
        <Transition>
          <button 
          name="AddNewMedicinePlan"
          @click="go('/medicine')"
          v-if="show_shurtcuts" class="btn btn-circle btn-success text-white text-lg shadow m-auto">
            <font-awesome :icon="faRectangleList" />
          </button>
        </Transition>
      </div>
      <div class="w-full h-full flex justify-center">
        <Transition>
          <button v-if="show_shurtcuts" class="pointer-events-auto btn btn-circle btn-success text-white text-lg shadow m-auto">
            <font-awesome :icon="faCalendar" />
          </button>
        </Transition>
      </div>
      <div class="w-full h-full flex justify-center">
        <button class="pointer-events-auto btn btn-circle btn-success shadow m-auto text-white text-lg" @click="show_shurtcuts=!show_shurtcuts">
          <font-awesome :icon="faGear" />
        </button>
      </div>
    </div>
</template>
<script setup>
import { faPills, faRectangleList, faCalendar, faGear } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { go } = useLocaleRouter()
const show_shurtcuts = ref(true)
</script>

<style scoped>
/* nav iconları animasyon alabilir özel css ile*
/* we will explain what these classes do next! */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>