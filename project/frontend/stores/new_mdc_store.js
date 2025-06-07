import { defineStore } from 'pinia';

export const useNewMdcStore = defineStore('new_mdc_store', {
  state: () => ({
    id: null,
    medicine_name: '',
    medicine_notes: '',
    start_date: '',
    end_date: '',
    weekly_dose_plans: [],
    medicine_dose_unit: 'miligram',
    medicine_dose_amount: 1,
    dose_amount: 1,
    dose_unit: 'miligram',
    frequency: 'daily',

    dose_times:[],
    // is vaild form START
    vaild_form_1: false, 
    vaild_form_2: false, 
    vaild_form_3: false, 
    vaild_form_4: false, 
    // is vaild form END
    form_index: 0,
    
    // Schedule-start
    schedules: [],
    editIndex: null,
    dose_unit_list: [
      { param: "ui", value: "UI" },
      { param: "microgram", value: "MCG" },
      { param: "miligram", value: "MG" },
      { param: "gram", value: "GR" },
      { param: "mililitre", value: "ML" },
      { param: "pieces", value: "Tane" },
      { param: "amp", value: "Ampül" },
      { param: "drop", value: "Damla" },
    ],
  }),
  getters: {
    sortedSchedules(state) {
      return [...state.schedules].sort((a, b) => new Date(a.start_date) - new Date(b.start_date))
    },
  },
  actions: {
    async save_diff() {
        const { $api } = useNuxtApp()
        const dif = await $api(this.id !== null ? `/medication/medications/${this.id}/`:'/medication/medications/create/'
        ,{
        method: this.id !== null ? 'PUT':'POST',
        body: {
            name: this.medicine_name,
            default_dose_amount: this.medicine_dose_amount,
            default_dose_unit: this.medicine_dose_unit, 
            // days_of_week: get_day_index_from_list(this.days_of_week),
                    //             "start_date": dayjs(this.start_date).format('YYYY-MM-DD'),
                    // "end_date": dayjs(this.end_date).format('YYYY-MM-DD'),
            "schedules": this.sortedSchedules,
          }
        })
        return dif
    },
    refull_self(exist_medication){
      this.id = exist_medication.id
      this.medicine_name = exist_medication.name
      this.schedules = exist_medication.schedules
      this.medicine_dose_unit = exist_medication.default_dose_unit
      this.medicine_dose_amount = exist_medication.default_dose_amount

      // Object.assign(this, JSON.parse(JSON.stringify(exist_medication)))
    },
    resetForm() {
        this.id = null,
        this.medicine_name = '';
        this.medicine_notes = '';
        this.start_date = '';
        this.end_date = '';
        this.weekly_dose_plans = [];
        this.dose_times = [];
        this.schedules = [],
        this.dose_amount = 1;
        this.medicine_dose_unit = 'miligram';
        this.medicine_dose_amount = 1;
        this.dose_unit = 'miligram';
        this.frequency = 'daily';
        this.days_of_week = [];
        this.day_of_month = 1;
        this.interval = 1;
        this.doses_per_period = 0;
        this.vaild_form_1 = false;
        this.vaild_form_2 = false;
        this.vaild_form_3 = false;
        this.vaild_form_4 = false;
        this.form_index = 0;
    },
    addSchedule(schedule) {
      this.schedules.push(schedule)
    },
    updateSchedule(index, schedule) {
      this.schedules[index] = schedule
    },
    removeSchedule(index) {
      this.schedules.splice(index, 1)
    },
    isFormValid() {
        return this.vaild_form_1 && this.vaild_form_2 && this.vaild_form_3 && this.vaild_form_4;
    },
    resetEditIndex() {
      this.editIndex = null
    },
    setWeeklyDosePlan(plan) {
        this.weekly_dose_plans.push(plan);
    },

    removeWeeklyDosePlan(index) {
        this.weekly_dose_plans.splice(index, 1);
    },

    setDoseTime(time) {
        this.dose_times.push(time);
    },

    removeDoseTime(index) {
        this.dose_times.splice(index, 1);
    },
    isOverlapping(newSchedule) {
      const startA = new Date(newSchedule.start_date)
      const endA = newSchedule.end_date ? new Date(newSchedule.end_date) : new Date('9999-12-31')

      return this.schedules.some((s, i) => {
        if (this.editIndex !== null && i === this.editIndex) return false

        const startB = new Date(s.start_date)
        const endB = s.end_date ? new Date(s.end_date) : new Date('9999-12-31')

        return startA <= endB && startB <= endA
      })
    },
  },
});

