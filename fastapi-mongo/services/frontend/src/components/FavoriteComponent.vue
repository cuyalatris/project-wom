<template>
    <div id="connexionTitle">
        <h2>Your favorite movies {{ text }}</h2>
        films déjà vus
        <ul id="example-1">
            <li v-for="item in vus" :key="item.title">
                {{ item.title }}
            </li>
        </ul>
        films préférés
        <ul id="example-1">
            <li v-for="item in preferes" :key="item.title">
                {{ item.title }}
            </li>
        </ul>
        genres préférés444
        <ul id="example-1">
            <li v-for="item in idGenre" :key="item">
                {{ item }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { store } from './../store.js'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            isDisabled: true,
            text : '',
            genre : '',
            idGenre:'',
            vus : [],
            idVus: ['tt1877830','tt0111161'],
            preferes : [],
            film : '',
            idPreferes: ['tt1877830','tt0111161','tt0068646'],
            idUser: '62488f129310318cdc2aff1c',
            userData: {},
            store
        }
    },
     mounted () {
        this.userData = this.getUserData()._id
        //this.idUser = récupérer l'id de l'user
        axios.get("/user/"+this.userData)
            .then(response => (this.idGenre = response.data.genre))
        axios.get("/user/"+this.userData)
            .then(response => (this.getMovieInfoVus(response.data.filmsVue)))
        axios.get("/user/"+this.userData)
            .then(response => (this.getMovieInfoPreferes(response.data.filmsPrefere)))
        
        
            
          //  .then(response => (this.infoUser = response))
     },
    methods: {
        getUserInfo() {
            axios.get("/user/"+this.idUser)
            .then(response => (this.infoUser = response))
        },
        getMovieInfoPreferes(tabmovie) {
            for (let index = 0; index < tabmovie.length; index++) {
                axios.get("/movie/"+tabmovie[index])
                .then(response => (this.preferes.push(response.data)))
            }           

        },
        getMovieInfoVus(tabmovie) {
            for (let index = 0; index < tabmovie.length; index++) {
                axios.get("/movie/"+tabmovie[index])
                .then(response => (this.vus.push(response.data)))
            }           

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
#connexionTitle {
    display: flex;
    align-items: center;
    justify-content: center;
}
#connexionForm {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>