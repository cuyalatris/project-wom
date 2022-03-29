import motor.motor_asyncio
from bson.objectid import ObjectId
MONGO_DETAILS = "mongodb://fastapi-mongo_mongodb_1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.movies

movies_collection = database.get_collection("movies_collection")


# helpers


def movie_helper(movie) -> dict:
    return {
        "id": str(movie["_id"]),
        "fullname": movie["fullname"],
        "genre": movie["genre"],
        "director": movie["director"],
        "year": movie["year"],
        "lienImage": movie["lienImage"],
        "duree": movie["duree"],
    }



# Retrieve all movies present in the database
async def retrieve_movies():
    movies = []
    async for movie in movies_collection.find():
        movies.append(movie_helper(movie))
    return movies


# Add a new movie into to the database
async def add_movie(movie_data: dict) -> dict:
    movie = await movies_collection.insert_one(movie_data)
    new_movie = await movies_collection.find_one({"_id": movie.inserted_id})
    return movie_helper(new_movie)


# Retrieve a movie with a matching ID
async def retrieve_movie(id: str) -> dict:
    movie = await movies_collection.find_one({"_id": ObjectId(id)})
    if movie:
        return movie_helper(movie)


# Update a movie with a matching ID
async def update_movie(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    movie = await movies_collection.find_one({"_id": ObjectId(id)})
    if movie:
        updated_movie = await movies_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_movie:
            return True
        return False


# Delete a movie from the database
async def delete_movie(id: str):
    movie = await movies_collection.find_one({"_id": ObjectId(id)})
    if movie:
        await movies_collection.delete_one({"_id": ObjectId(id)})
        return True