<template>
  <div>
    <h1>{{movie.title}}</h1>
    <div>
        <span>{{ movie.plot}}</span>
    </div>
    <div>
        <span>Rating : {{movie.imDbRating}}</span>
    </div>
    <div>
        <span>Release Date : {{movie.releaseDate}}</span>
    </div>
    <div>
        <span>Runtime : {{movie.runtimeStr}}</span>
    </div>
    <div>
        <img :src="movie.image" style="width:200px">
    </div>
    <ui-icon-button @click="AddFilmPrefere(movie.id)" v-model="value1" :toggle="mdcIcon"> </ui-icon-button>
    <ui-icon-button @click="AddFilmVue(movie.id)">
        <template #default="{ onClass, offClass }" >
            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" :class="onClass">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" :class="offClass" >
            <path d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/>
            </svg>
        </template>
    </ui-icon-button>
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
            movie: [],
            idMovie:this.$route.params.idMovie,
            idUser : '624a02a246af61eb22fb92d2',
            test2 : false,
            test : false,
        }
    },
    mounted(){
        this.GetMovies(this.idMovie)
        //axios.get("/movie")
          //  .then(response => (this.movies = response))
    },
    methods: {
        GetMovies(idMovie) {
            axios.get("/movie/"+idMovie)
            .then((response) => (this.movie = response.data.data[0]))
            //.catch(e => console.log(e))
            console.log(this.movie)
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
            if (this.test) {
                //enlever le film de la liste des préférés
                axios.delete("user/prefere/"+this.idUser+"/"+movie+"/")
            } else {
                //ajouter le film dans la liste des préférés
                axios.put("/user/prefere/"+this.idUser+"/"+movie+"/")
            }
            this.test = !this.test
            //this.value1 = !this.value1
            //.then((response) => (this.movies = response.data.data[0]))
            
        },
        AddFilmVue(movie) {
            if (this.test2) {
                axios.delete("/user/"+this.idUser+"/"+movie)
            } else {
                axios.put("/user/"+this.idUser+"/"+movie)
            }
            this.test2 = !this.test2

            //axios.delete("user/prefere/"+this.idUser+"/"+movie)
            //.then((response) => (this.movies = response.data.data[0]))
        }
    },
    // props: {
    //     idMovie : String
    // }
}
</script>