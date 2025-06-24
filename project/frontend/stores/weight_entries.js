import { defineStore } from 'pinia'
import { useNuxtApp } from '#app'
import dayjs from 'dayjs'

export const useWeightEntryStore = defineStore('weightEntries', {
  state: () => ({
    entries: [],  // [{ id, weight, date }]
    loading: false,
    error: null,
  }),

  getters: {
    latestWeight: (state) => state.entries[0]?.weight || '-',

    weightChange: (state) => {
      if (state.entries.length < 2) return 0
      return (state.entries[0].weight - state.entries[1].weight).toFixed(1)
    },

    chartSeries: (state) => [
      {
        name: 'Kilo',
        data: [...state.entries].map(e => e.weight).reverse(),
      },
    ],

    chartCategories: (state) =>
      [...state.entries].map(e => e.date).reverse(),
  },

  actions: {
    async fetchEntries() {
      this.loading = true
      this.error = null
      const { $api } = useNuxtApp()

      try {
        const res = await $api('/health/weight/entries/')
        this.entries = res
          .map(e => ({
            ...e,
            date: dayjs(e.date).format('YYYY-MM-DD'),
          }))
          .sort((a, b) => new Date(b.date) - new Date(a.date))
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },

    async addEntry(weight, date) {
      if (!weight || weight <= 0) return

      const { $api } = useNuxtApp()

      try {
        const res = await $api('/health/weight/entries/', {
          method: 'POST',
          body: {
            weight: weight.toString(),
            date: dayjs(date).format('YYYY-MM-DD'),
          },
        })

        this.entries.unshift({
          ...res,
          date: dayjs(res.date).format('YYYY-MM-DD'),
        })
      } catch (err) {
        this.error = err
        throw err
      }
    },

    async deleteEntry(id) {
      const { $api } = useNuxtApp()

      try {
        await $api(`/health/weight/entries/${id}/`, {
          method: 'DELETE',
        })

        this.entries = this.entries.filter(e => e.id !== id)
      } catch (err) {
        this.error = err
        throw err
      }
    },
  },
})
