from fastapi import  FastAPI, APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.server.routes.params import *
from asyncio.base_subprocess import ReadSubprocessPipeProto
from urllib import response
import requests
import json
import copy

from src.server.database import (
    add_movie,
    delete_movie,
    retrieve_movie,
    retrieve_movies,
    update_movie,
)
from src.server.models.movies import (
    ErrorResponseModel,
    ResponseModel,
    MovieSchema,
    UpdateMoviesModel,
)

router = APIRouter()
    
@router.post("/", response_description="Movie data added into the database")
async def add_movie_data(movie: MovieSchema = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = await add_movie(movie)
    return ResponseModel(new_movie, "Movie added successfully.")

@router.get("/", response_description="Movies retrieved")
async def get_movies():
    movies = await retrieve_movies()
    if movies:
        return ResponseModel(movies, "movies data retrieved successfully")
    return ResponseModel(movies, "Empty list returned")


@router.get("/{id}", response_description="movie data retrieved")
async def get_movie_data(id):
    movie = await retrieve_movie(id)
    if movie:
        return ResponseModel(movie, "movie data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "movie doesn't exist.")


@router.put("/{id}")
async def update_movie_data(id: str, req: UpdateMoviesModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_movie = await update_movie(id, req)
    if updated_movie:
        return ResponseModel(
            "Movie with ID: {} name update is successful".format(id),
            "Movie name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the movie data.",
    )


@router.delete("/{id}", response_description="Movie data deleted from the database")
async def delete_movie_data(id: str):
    deleted_movie = await delete_movie(id)
    if deleted_movie:
        return ResponseModel(
            "Movie with ID: {} removed".format(id), "Movie deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Movie with id {0} doesn't exist".format(id)
    )

@router.get('/Movies/SearchMovie/{title}')
async def researchByTitle(title):
    response = requests.get(site + research_dico["SMovie"] + api_key + title).json()
    return response

@router.get('/Movies/GetTop250Movies')
async def researchTop250():
    test = ""
    response = requests.get(site + research_dico["TopMovies"] + api_key).json()
    for item in response["items"]:
        test += item["id"]+" , "
    return test

@router.get('/Movies/GetMostPopular')
async def researchMostPop():
    response = requests.get(site + research_dico["MostPopMovies"] + api_key).json()
    return response

@router.get('/All/SearchInAll/{expression}')
async def researchAll(expression):
    response = requests.get(site + research_dico["SAll"] + api_key + expression).json()
    return response

@router.get('/Movies/GetInfos/{id}')
async def getInfos(id):
    response = requests.get(site + research_dico["STitle"] + api_key + id + option).json()
    jb = copy.deepcopy(response)
    for cle, valeur in jb.items():
        if cle not in list_champ :
            response.pop(cle)
    await add_movie_data(response)
    return response
    #add_movie_data(response):
