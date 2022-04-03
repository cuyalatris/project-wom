from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field

from src.server.database import (
    add_genre_user,
    add_movie_userPrefere,
    add_movie_userVue,
    add_user,
    delete_movie_userPrefere,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from src.server.models.users import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

class UserLogInSchema(BaseModel):
    email: EmailStr = Field(...)
    password : str = Field(...)
    
router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user.password = get_password_hash(user.password)
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")

@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{email}", response_description="user data retrieved")
async def get_user_data(email):
    user = await retrieve_user(email)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.put("/prefere/{id}/{newMovie}/")
async def update_user_moviePref(id: str, newMovie: str):
    #req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await add_movie_userPrefere(id, newMovie)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.put("/delete/prefere/{id}/{newMovie}/")
async def delete_user_moviePref(id: str, newMovie: str):
    #req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await delete_movie_userPrefere(id, newMovie)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.put("/genre/{id}/{genre}/")
async def update_user_genre(id: str, newGenre: str):
    #req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await add_genre_user(id, newGenre)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )
@router.put("/delete/genre/{id}/{genre}/")
async def update_user_moviePref(id: str, newMovie: str):
    #req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await delete_movie_userPrefere(id, newMovie)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.put("/{id}/{newMovie}")
async def update_user_movieVue(id: str, newMovie: str):
    #req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await add_movie_userVue(id, newMovie)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
    )

SECRET_KEY = "7691c96b23e87a657ef0c1e80f4f6332cf875324d3f1f24e8dc6c8b134480a23"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "tris": {
        "userName": "tris",
        "email": "tr@gmail.com",
        "password": "$2b$12$WtcZG4NAu8NQBzpSxDF4D.wfr8V3.Uogs9CZJScXzYegUej9dJVFW",
    },
    "tros": {
        "userName": "tros",
        "email": "tra@gmail.com",
        "password": "$2b$12$WtcZG4NAu8NQBzpSxDF4D.wfr8V3.Uogs9CZJScXzYegUej9dJVFW",
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    userName: Optional[str] = None
    
class UserInDb(UserSchema):
    password:str
    
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/token')

@router.get("/hashtest/")
async def hashPasswordTest():
    return pwd_context.hash('secret')

def verify_password(plain_password, hashed_password):
    return(pwd_context.verify(plain_password, hashed_password))

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username:str):
    for user in db:
        userName_value = user["email"]
        if userName_value == username:
            return UserInDb(**user)
    # if username in db:
    #     user_dict = db[username]
    #     return UserInDb(**user_dict)
    
def authenticate_user(fake_db, userName: str, password: str):
    user = get_user(fake_db, userName)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userName: str = payload.get("sub")
        if userName is None:
            raise credentials_exception
        token_data = TokenData(userName=userName)
    except JWTError:
        raise credentials_exception
    users_db = await get_users()
    users_db_data = users_db["data"][0]
    user = get_user(users_db_data, username=token_data.userName)
    # user = get_user(fake_users_db, userName=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user

@router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
async def login_for_access_token(UserLogIn: UserLogInSchema = Body(...)):
    users_db = await get_users()
    users_db_data = users_db["data"][0]
    # form_data: OAuth2PasswordRequestForm = Depends()
    # form_data.username = UserLogIn.email
    # form_data.password = UserLogIn.password
    user = authenticate_user(users_db_data, UserLogIn.email, UserLogIn.password)
    # user = authenticate_user(users_db_data, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
    
@router.get("/users/me/", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user

@router.get("/users/me/items/")
async def read_own_items(current_user: UserSchema = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.userName}]