import { reactive } from 'vue'

export const store = reactive({
    access_token: '',
    set_access_token(user_access_token) {
        this.access_token = user_access_token
    },
    get_access_token() {
        return this.access_token
    }
})