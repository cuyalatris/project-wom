<template>
    <div>   
        <ui-grid class="gridou" position="center">
            <ui-grid-cell v-for="i in movies" :key="i" class="demo-cell" columns="2">
                <div>
                    <span>{{i.id}}</span>
                </div>
            </ui-grid-cell>
        </ui-grid>
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'

export default {
    data() {
        return {
            movies:'',
        }
    },
    methods: {
        GetMovies() {
            axios.get("/movie/")
            .then((response) => {this.movies = response.data})
            //.catch(e => console.log(e))
            console.log(this.movies)
        }
    },
    mounted() {
        this.GetMovies()
    },
}
</script>
