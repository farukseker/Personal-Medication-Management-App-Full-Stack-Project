// stores/user.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user_store', {
  state: () => ({
    profile_picture: '',
    first_name: '',
    last_name: '',
  })
})
