<template>
    <div>   
        <ui-grid class="gridou" position="center">
            <ui-grid-cell v-for="i in movies" :key="i" class="demo-cell" columns="2">
                <div class="onemovie">
                    <div class="img_container">
                        <img v-bind:src="i.image">
                    </div>
                    <div class="Titre">
                        <span>{{i.title}}</span>
                    </div>
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
            movies :[
            {
                "_id": "62459883eb47253124acbf8f",
                "id": "tt1877830",
                "title": "The Batman",
                "fullTitle": "The Batman (2022)",
                "type": "Movie",
                "year": "2022",
                "image": "https://imdb-api.com/images/original/MV5BMDdmMTBiNTYtMDIzNi00NGVlLWIzMDYtZTk3MTQ3NGQxZGEwXkEyXkFqcGdeQXVyMzMwOTU5MDk@._V1_Ratio0.6751_AL_.jpg",
                "releaseDate": "2022-03-04",
                "runtimeStr": "2h 56min",
                "plot": "When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.",
                "directors": "Matt Reeves",
                "writers": "Matt Reeves, Peter Craig, Bill Finger",
                "stars": "Robert Pattinson, Zoë Kravitz, Jeffrey Wright",
                "genres": "Action, Crime, Drama",
                "companies": "Warner Bros., 6th & Idaho Productions, DC Comics",
                "countries": "USA",
                "languages": "English",
                "contentRating": "PG-13",
                "imDbRating": "8.3",
                "tagline": "Unmask The Truth",
                "keywords": "superhero,batman character,based on comic,dc comics,gotham city",
                "similars": [
                {
                    "id": "tt0468569",
                    "title": "The Dark Knight",
                    "image": "https://imdb-api.com/images/original/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "9.1"
                },
                {
                    "id": "tt0372784",
                    "title": "Batman Begins",
                    "image": "https://imdb-api.com/images/original/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.3"
                },
                {
                    "id": "tt10872600",
                    "title": "Spider-Man: No Way Home",
                    "image": "https://imdb-api.com/images/original/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.5"
                },
                {
                    "id": "tt1345836",
                    "title": "The Dark Knight Rises",
                    "image": "https://imdb-api.com/images/original/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt7286456",
                    "title": "Joker",
                    "image": "https://imdb-api.com/images/original/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt1464335",
                    "title": "Uncharted",
                    "image": "https://imdb-api.com/images/original/MV5BMWEwNjhkYzYtNjgzYy00YTY2LThjYWYtYzViMGJkZTI4Y2MyXkEyXkFqcGdeQXVyNTM0OTY1OQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "6.7"
                },
                {
                    "id": "tt0096895",
                    "title": "Batman",
                    "image": "https://imdb-api.com/images/original/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "7.5"
                },
                {
                    "id": "tt4154796",
                    "title": "Avengers: Endgame",
                    "image": "https://imdb-api.com/images/original/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt2463208",
                    "title": "The Adam Project",
                    "image": "https://imdb-api.com/images/original/MV5BOWM0YWMwMDQtMjE5NS00ZTIwLWE1NWEtODViMWZjMWI2OTU3XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "6.7"
                },
                {
                    "id": "tt4154756",
                    "title": "Avengers: Infinity War",
                    "image": "https://imdb-api.com/images/original/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.5"
                },
                {
                    "id": "tt1160419",
                    "title": "Dune",
                    "image": "https://imdb-api.com/images/original/MV5BN2FjNmEyNWMtYzM0ZS00NjIyLTg5YzYtYThlMGVjNzE1OGViXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.1"
                },
                {
                    "id": "tt13560574",
                    "title": "X",
                    "image": "https://imdb-api.com/images/original/MV5BMTJiMmE5YWItOWZjYS00YTg0LWE0MTYtMzg2ZTY4YjNkNDEzXkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_Ratio0.8019_AL_.jpg",
                    "imDbRating": "7.3"
                }
                ]
            },
            {
                "_id": "62459883eb47253124acbf8f",
                "id": "tt1877831",
                "title": "The Batman WISH",
                "fullTitle": "The Batman (2022)",
                "type": "Movie",
                "year": "2022",
                "image": "https://imdb-api.com/images/original/MV5BMDdmMTBiNTYtMDIzNi00NGVlLWIzMDYtZTk3MTQ3NGQxZGEwXkEyXkFqcGdeQXVyMzMwOTU5MDk@._V1_Ratio0.6751_AL_.jpg",
                "releaseDate": "2022-03-04",
                "runtimeStr": "2h 56min",
                "plot": "When the Riddler, a sadistic serial killer, begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption and question his family's involvement.",
                "directors": "Matt Reeves",
                "writers": "Matt Reeves, Peter Craig, Bill Finger",
                "stars": "Robert Pattinson, Zoë Kravitz, Jeffrey Wright",
                "genres": "Action, Crime, Drama",
                "companies": "Warner Bros., 6th & Idaho Productions, DC Comics",
                "countries": "USA",
                "languages": "English",
                "contentRating": "PG-13",
                "imDbRating": "8.3",
                "tagline": "Unmask The Truth",
                "keywords": "superhero,batman character,based on comic,dc comics,gotham city",
                "similars": [
                {
                    "id": "tt0468569",
                    "title": "The Dark Knight",
                    "image": "https://imdb-api.com/images/original/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "9.1"
                },
                {
                    "id": "tt0372784",
                    "title": "Batman Begins",
                    "image": "https://imdb-api.com/images/original/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.3"
                },
                {
                    "id": "tt10872600",
                    "title": "Spider-Man: No Way Home",
                    "image": "https://imdb-api.com/images/original/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.5"
                },
                {
                    "id": "tt1345836",
                    "title": "The Dark Knight Rises",
                    "image": "https://imdb-api.com/images/original/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt7286456",
                    "title": "Joker",
                    "image": "https://imdb-api.com/images/original/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt1464335",
                    "title": "Uncharted",
                    "image": "https://imdb-api.com/images/original/MV5BMWEwNjhkYzYtNjgzYy00YTY2LThjYWYtYzViMGJkZTI4Y2MyXkEyXkFqcGdeQXVyNTM0OTY1OQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "6.7"
                },
                {
                    "id": "tt0096895",
                    "title": "Batman",
                    "image": "https://imdb-api.com/images/original/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "7.5"
                },
                {
                    "id": "tt4154796",
                    "title": "Avengers: Endgame",
                    "image": "https://imdb-api.com/images/original/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.4"
                },
                {
                    "id": "tt2463208",
                    "title": "The Adam Project",
                    "image": "https://imdb-api.com/images/original/MV5BOWM0YWMwMDQtMjE5NS00ZTIwLWE1NWEtODViMWZjMWI2OTU3XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "6.7"
                },
                {
                    "id": "tt4154756",
                    "title": "Avengers: Infinity War",
                    "image": "https://imdb-api.com/images/original/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.5"
                },
                {
                    "id": "tt1160419",
                    "title": "Dune",
                    "image": "https://imdb-api.com/images/original/MV5BN2FjNmEyNWMtYzM0ZS00NjIyLTg5YzYtYThlMGVjNzE1OGViXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_Ratio0.6763_AL_.jpg",
                    "imDbRating": "8.1"
                },
                {
                    "id": "tt13560574",
                    "title": "X",
                    "image": "https://imdb-api.com/images/original/MV5BMTJiMmE5YWItOWZjYS00YTg0LWE0MTYtMzg2ZTY4YjNkNDEzXkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_Ratio0.8019_AL_.jpg",
                    "imDbRating": "7.3"
                }
                ]
            }
            ]
            //movies:[],
        }
    },
    methods: {
        GetMovies() {
            axios.get("/movie/")
            .then((response) => {this.movies.push(response.data)})
            //.catch(e => console.log(e))
            console.log(this.movies)
        },
        checkedMonuted(){
            console.log("Is mounted")
        }
    },
    mounted(){
        this.checkedMonuted()
        this.GetMovies()
    }
}
</script>

<style scoped lang="scss">
    
</style>
