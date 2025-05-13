import { defineStore } from 'pinia';


export const useUserStore = defineStore('use_user_store', {
    state: () => ({
        username: '',
        email: ''
    }),
    actions:
    {
        
    }
});
