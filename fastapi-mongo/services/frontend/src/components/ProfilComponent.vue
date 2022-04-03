<template>
    <div>
    
        <h1>{{ infoUser.userName }}</h1>
    
        <h2>{{ infoUser.email }}</h2>
    
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            isDisabled: true,
            infoUser:'',
            idUser : '62488f129310318cdc2aff1c'
        }
    },
     mounted () {
        //this.idUser = récupérer l'id de l'user
        axios.get("/user/"+this.idUser)
            .then(response => (this.infoUser = response.data.data[0]))
        
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