import { defineStore } from 'pinia';

export const useMedicineFormStore = defineStore('medicine_form_store', {
  state: () => ({
    medicine_name: '',
    medicine_notes: '',
    hunger_situation: 'non', // Fark etmez
    scale_type: 'scale',
    often_list: [],
    increasing_ranges: [],
    weight_type: '',
    isLoading: false,
    start_date: '',
    end_date: '',
    remind_times: [],
    // temp values
    increasing_range: '',
    direction_range: '',
    direction_range_type: ''
  }),
  actions: {
    addRemindTime(new_time) {
      if (this.remind_times && !this.remind_times.includes(new_time)) {
        this.remind_times.push(new_time)
      }
    },
    removeRemindTime(index) {
      this.remind_times.splice(index, 1)
    },
    startLoading() {
      this.isLoading = true;
    },
    stopLoading() {
      this.isLoading = false;
    },
  },
});

