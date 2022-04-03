import motor.motor_asyncio
from bson.objectid import ObjectId
MONGO_DETAILS = "mongodb://fastapi-mongo_mongodb_1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.movies


#########################################
#       Movies_collection
#########################################
movies_collection = database.get_collection("movies_collection")


# helpers


def movie_helper(movie) -> dict:
    return {
        "_id": str(movie["_id"]),
        "id": movie["id"],
        "title": movie["title"],
        "fullTitle": movie["fullTitle"],
        "type": movie["type"],
        "year": movie["year"],
        "image": movie["image"],
        "releaseDate": movie["releaseDate"],
        "runtimeStr": movie["runtimeStr"],
        "plot": movie["plot"],
        "directors": movie["directors"],
        "writers": movie["writers"],
        "stars": movie["stars"],
        "genres": movie["genres"],
        "companies": movie["companies"],
        "countries": movie["countries"],
        "languages": movie["languages"],
        "contentRating": movie["contentRating"],
        "imDbRating": movie["imDbRating"],
        "tagline": movie["tagline"],
        "keywords": movie["keywords"],
        "similars": movie["similars"],
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
    movie = await movies_collection.find_one({"id": id})
    if movie:
        return movie_helper(movie)

# Retrieve a movie with a matching name
async def retrieve_movie_name(name: str) -> dict:
    movie = await movies_collection.find_one({"title": name})
    if movie:
        return movie_helper(movie)

# Update a movie with a matching ID
async def update_movie(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    movie = await movies_collection.find_one({"id": id})
    if movie:
        updated_movie = await movies_collection.update_one(
            {"id": id}, {"$set": data}
        )
        if updated_movie:
            return True
        return False


# Delete a movie from the database
async def delete_movie(id: str):
    movie = await movies_collection.find_one({"id": id})
    if movie:
        await movies_collection.delete_one({"id": id})
        return True

#########################################
#       Users
#########################################

users = database.get_collection("users")


# helpers


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "userName": user["userName"],
        "email": user["email"],
        "password": user["password"],
        "genre" : user["genre"],
        "filmsVue" : user["filmsVue"],
        "filmsPrefere" : user["filmsPrefere"]
    }



# Retrieve all user present in the database
async def retrieve_users():
    allUsers = []
    async for user in users.find():
        allUsers.append(user_helper(user))
    return allUsers


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await users.insert_one(user_data)
    new_user = await users.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Retrieve a user with a matching name
async def retrieve_user_name(name: str) -> dict:
    user = await users.find({"userName": name})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False
# Update a fav genre in the list of the user with a matching ID
async def add_genre_user(id: str, data: str):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$push": {"genre" : data}} , upsert = True
        )
        if updated_user:
            return True
        return False
# Update a movie seen in the list of the user with a matching ID
async def add_movie_userVue(id: str, data: str):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$push": {"filmsVue" : data}} , upsert = True
        )
        if updated_user:
            return True
        return False

async def delete_movie_userVue(id: str, data: str):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$pull": {"filmsVue" : data}} , upsert = True
        )
        if updated_user:
            return True
        return False



async def add_movie_userPrefere(id: str, data: str):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$push": {"filmsPrefere" : data}} , upsert = True
        )
        if updated_user:
            return True
        return False

async def delete_movie_userPrefere(id: str, data: str):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await users.update_one(
            {"_id": ObjectId(id)}, {"$pull": {"filmsPrefere" : data}} , upsert = True
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await users.find_one({"_id": ObjectId(id)})
    if user:
        await users.delete_one({"_id": ObjectId(id)})
        return True