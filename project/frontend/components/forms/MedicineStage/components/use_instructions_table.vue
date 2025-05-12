<template>
<div class="overflow-x-auto w-full">
    <label class="label">
        Tarife Tablosu
    </label>
    <table class="table table-xs md:table-md table-zebra" v-if="medicine_store.increasing_ranges.length > 0">
        <!-- head -->
        <thead>
        <tr>
            <th>#</th>
            <th>Miktar</th>
            <th>Aralık</th>
            <th>Başlangıç</th>
            <th class="hidden md:block">Bitiş</th>
            <th>Sil</th>
        </tr>
        </thead>
        <tbody>
            <tr v-for="(_increasing_range, index) in medicine_store.increasing_ranges">
                <th>{{ index + 1 }}.</th>
                <td>{{ _increasing_range.increasing }} {{ _increasing_range.weight_type }}</td>
                <td >{{ _increasing_range.range_type_tr_name }} {{ _increasing_range.range }}</td>
                <td>{{ _increasing_range.start.format('YYYY-MM-DD') }}</td>
                <td class="hidden md:block">{{ _increasing_range.end.format('YYYY-MM-DD') }}</td>
                <td>
                    <button class="btn btn-sm btn-error text-white" @click="$emit('del_increasing', index)">x</button>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script setup>
import { useMedicineFormStore } from '@/stores/medicine_form_store.js'

defineEmits(['del_increasing'])

const medicine_store = useMedicineFormStore()

</script>