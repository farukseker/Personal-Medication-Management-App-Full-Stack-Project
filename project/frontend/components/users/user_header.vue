<template>
    <section class="flex gap-2 justify-center bg-base-300 rounded px-4 py-2 shadow">
        <article>
            <div class="w-[36px] h-[36px] bg-fuchsia-500 rounded-full shadow"></div>
        </article>
        <article class="my-auto w-full">
            <h2 class="font-semibold my-auto text-xl md:text-2xl">Hi, Faruk</h2> 
        </article>
        <article class="m-auto text-xl">
            <font-awesome :icon="faBars" />
        </article>
    </section>
</template>

<script setup>
import { faBars } from '@fortawesome/free-solid-svg-icons'
</script>