<template>
    <div>   
        <ui-grid class="gridou" position="center">

            <ui-grid-cell v-for="i in movies" :key="i" class="demo-cell" columns="2">
                <div class="onemovie">
                    <div class="img_container">
                        <img v-bind:src="i.image" style="width:100%; height:100%">
                    </div>
                    <div class="Titre">
                        <span>{{i.title}}</span>
                    </div>
                        <ui-icon-button @click="AddFilmPrefere(i.id)" v-model="value1" :toggle="mdcIcon"> </ui-icon-button>
                        <ui-icon-button>
                        <template #default="{ onClass, offClass }" >
                            <svg @change="AddFilmVue(i.id, true)" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" :class="onClass">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z" />
                            </svg>
                            <svg @change="AddFilmVue(i.id, false)" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" :class="offClass" >
                            <path d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/>
                            </svg>
                        </template>
                        </ui-icon-button>
                </div>
            </ui-grid-cell>
        </ui-grid>
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
const mdcIcon = {
  on: 'favorite',
  off: 'favorite_border'
};
export default {
    data() {
        return {
            mdcIcon,
            movies: [],
            //value1: false,
            //value2: true,
            test : false,
            idUser : '62488f129310318cdc2aff1c'
        }
    },
    mounted(){
        this.GetMovies()
        //axios.get("/movie")
          //  .then(response => (this.movies = response))
    },
    methods: {
        GetMovies() {
            axios.get("/movie")
            .then((response) => (this.movies = response.data.data[0]))
            //.catch(e => console.log(e))
            console.log(this.movies)
        },
        checkedMonuted(){
            console.log("Is mounted")
        },
        isFilmVue(movie, bool) {
            axios.get("user/"+this.idUser+"/"+movie)
            .then((response) => (bool = response))
            return bool
        },
        isFilmPref(movie, bool) {
            axios.get("user/prefere/"+this.idUser+"/"+movie)
            .then((response) => (bool = response))
            return bool
        },
        AddFilmPrefere(movie){
            this.test = this.isFilmPref(movie, true)
            if (!this.test) {
                //enlever le film de la liste des préférés
                axios.delete("user/prefere/"+this.idUser+"/"+movie)
            } else {
                //ajouter le film dans la liste des préférés
                axios.put("/user/prefere/"+this.idUser+"/"+movie)
            }
            //this.value1 = !this.value1
            //.then((response) => (this.movies = response.data.data[0]))
            
        },
        AddFilmVue(movie, test) {
            if (!test) {
                axios.delete("/user/"+this.idUser+"/"+movie)
            } else {
                axios.put("/user/"+this.idUser+"/"+movie)
            }
            //axios.delete("user/prefere/"+this.idUser+"/"+movie)
            //.then((response) => (this.movies = response.data.data[0]))
        }

    }
}
</script>

<style scoped lang="scss">
    @use 'balm-ui/components/icon-button/icon-button';
</style>
