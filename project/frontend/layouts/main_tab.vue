<template>
<UNotifications />

<div class="font-[Roboto] flex flex-1 flex-col w-full">
    <div class="pb-20">
        <div class="p-4 space-y-4 max-w-md mx-auto">
            <div class="flex flex-col gap-4 flex-1">
            <div class="flex justify-between items-center">
                <h1 class="text-xl font-bold">{{ $t('index.title') }}</h1>
                <button 
                @click="go('/settings')"
                class="btn btn-ghost btn-circle text-2xl p-0">
                <img class="w-[36px] h-[36px] object-cover rounded-full shadow-md" src="/pp.jpg" alt="">
                </button>
            </div>
            </div>

            <div class="flex w-full">
            <h2 class="text-lg font-semibold mb-2 w-full">{{ $t('index.today') }}, {{ today }}</h2>
            <button class="btn btn-primary btn-sm" @click="go_new_medicine_form">
                + {{ $t('index.add_medication') }}
            </button>
            </div>

            <nav class="tabs tabs-lift tabs-md tabs-top">
            <button @click="go('/tab/medications')" class="tab hover:text-green-500 flex gap-2" :class="isPathEqual('/')">
                <font-awesome :icon="faPills" /> {{ $t('index.medications') }}
            </button>
            <button @click="go('/tab/counters')" class="tab hover:text-green-500 flex gap-2" :class="isPathEqual('counter')">
                <font-awesome :icon="faPlus" /> {{ $t('index.counter') }}
            </button>
            <button @click="go('/tab/water_tracking')" class="tab hover:text-green-500 flex gap-2" :class="isPathEqual('water')">
                <font-awesome :icon="faGlassWater" /> {{ $t('index.water_tracking') }}
            </button>
            <button @click="go('/tab/weight_tracking')" class="tab hover:text-green-500 flex gap-2" :class="isPathEqual('weight')">
                <font-awesome :icon="faGlassWater" /> {{ $t('index.weight_tracking') }}
            </button>
            </nav>

            <section>
                <slot />
            </section>
        </div>
    </div>
    <NavBottomNav />
</div>
</template>

<script setup>
definePageMeta({
  pageTransition: {
    name: 'rotate'
  }
})
onMounted(() => {
    const theme = localStorage.getItem('theme') || 'light'
    document.documentElement.setAttribute('data-theme', theme)
})


</script>
<style>
.rotate-enter-active,
.rotate-leave-active {
  transition: all 0.4s;
}
.rotate-enter-from,
.rotate-leave-to {
  opacity: 0;
  transform: rotate3d(1, 1, 1, 15deg);
}
</style>

