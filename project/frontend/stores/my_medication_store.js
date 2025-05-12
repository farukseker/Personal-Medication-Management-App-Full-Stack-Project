import { defineStore } from 'pinia';


export const useMyMedicationStore = defineStore('my-medication-store', {
  state: () => ({
    medicationListisLoading: false,
    medicationList: [],
    nextMedicationList: [],
    myMedicationList: []
  }),
  actions: {
      async getMyMedicationList() {
        if (this.myMedicationList.length > 0) {
            return this.myMedicationList
        }
        const { $api } = useNuxtApp()
        const response = await $api('/medication/my-medication-list')
        this.myMedicationList = response
        return this.myMedicationList
    },
    async getMedicationList() {
        if (this.medicationList.length > 0) {
            return this.medicationList
        }
        const { $api } = useNuxtApp()
        const response = await $api('/medication/my-medication-history')
        this.medicationList = response
        return this.medicationList
    },
      async getNextMedicationList() {
        if (this.nextMedicationList.length > 0) {
            return this.nextMedicationList
        }
        const { $api } = useNuxtApp()
        const response = await $api('/medication/next-medications-list')
        this.nextMedicationList = response
        return this.nextMedicationList
    },
    async deleteMedicationObjFromIndex(index) {
       const medication = this.medicationList[index]
       if (!medication) {return;}
       const { $api } = useNuxtApp()
       await $api(`/medication/delete-medications-history/${medication.id}`, {
        method: "DELETE"
       })
       await this.reload_medication_list()
       await this.reload_next_medication_list()
    },

    async addUsedMedication(pyload) {
      // pyload: {dosage: '', medication: 'medication_id'}
      const { $api } = useNuxtApp()
      await $api('/medication/add-medications-history', {
        method: 'POST',
        body: pyload
      })
      await this.reload_medication_list()
      await this.reload_next_medication_list()
    },

    stopLoading() {
      this.isLoading = false;
    },
    async reload_medication_list () {
      this.medicationList = []
      await this.getMedicationList()
    },
      async reload_my_medication_list () {
      this.myMedicationList = []
      await this.getMyMedicationList()
    },
    async reload_next_medication_list () {
      this.nextMedicationList = []
      await this.getNextMedicationList()
    }


  },
});
