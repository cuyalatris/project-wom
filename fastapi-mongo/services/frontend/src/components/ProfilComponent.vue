<template>
    <div>
    
        <h1>{{ infoUser.userName }}</h1>
    
        <h2>{{ infoUser.email }}</h2>
    
    </div>
</template>

<script>
import { store } from './../store.js'
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            isDisabled: true,
            infoUser:'',
            idUser : '62488f129310318cdc2aff1c',
            userData : {},
            store
        }
    },
     mounted () {
        this.userData = this.getUserData()
        //this.idUser = récupérer l'id de l'user
        axios.get("/user/"+this.userData.email)
            .then(response => (this.infoUser = response.data))
        
     },
    methods: {
        getUserInfo() {
            axios.get("/user/"+this.idUser)
            .then(response => (this.infoUser = response))
        },
        ChangePassword() {
        // reformat the payload from [{name: Age, value: 10}, ...] to {Age:10, ...}
            axios.get("/user/"+this.idUser)
            .then(response => (this.infoUser = response))
            //.then()
            //.catch(e => console.log(e))
        },
        getUserData() {
            this.current_access_token = store.get_access_token()
            this.current_user_data = axios.get('/user/users/me/', {
                params: {
                token: this.current_access_token
                }
            })
                .then((response) => {
                console.log(response.data)
                })
            console.log(this.current_user_data)
            return this.current_user_data
        }

    }
}
</script>

<style scoped lang="scss">
#profileTitle {
    display: flex;
    align-items: center;
    justify-content: center;
}
#profileForm {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>