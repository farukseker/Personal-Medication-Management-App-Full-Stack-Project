<template>
{{ $t('index.today') }}, {{ today }} {{ $t(`month_names.${today_month_name}`) }}
</template>

<script setup>
import dayjs from 'dayjs'

const today = ref(null)
const today_month_name = ref(null)

onMounted(()=>{
    today.value = dayjs().format('DD')
    today_month_name.value = dayjs().format('MMMM')
})
</script>