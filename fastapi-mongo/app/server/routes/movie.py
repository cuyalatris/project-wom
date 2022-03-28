from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_movie,
    delete_movie,
    retrieve_movie,
    retrieve_movies,
    update_movie,
)
from app.server.models.movies import (
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