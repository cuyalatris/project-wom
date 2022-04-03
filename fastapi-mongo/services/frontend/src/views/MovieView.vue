<template>
  <div>
    <h1>Coucou c'est la vue du film</h1>
    <div class="Moviename">
        <span>Nom : {{movie.title}}</span>
    </div>
    <div>
        <span>Plot : {{movie.plot}}</span>
    </div>
    <div>
        <span>Rating : {{movie.imDbRating}}</span>
    </div>
    <div>
        <img :src="movie.image">
    </div>
    <div>
        <span>Release Date : {{movie.releaseDate}}</span>
    </div>
    <div>
        <span>Runtime : {{movie.runtimeStr}}</span>
    </div>
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
            //value1: false,
            value2: true,
            idUser : '62488f129310318cdc2aff1c'
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
        checkedMonuted(){
            console.log("Is mounted")
        }
    },
    // props: {
    //     idMovie : String
    // }
}
</script>