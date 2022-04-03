import time
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    userName: str = Field(...)
    email: EmailStr = Field(...)
    password : str = Field(...)
    genre : Optional[List[str]]
    filmsVue : Optional[List[str]]
    filmsPrefere :  Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "userName": "Jean",
                "email": "jean@jean.com",
                "password": "PeterPan4",
                "genre" : ["Action","Adventure"],
                "filmsVue" : ["tt1877830"],
                "filmsPrefere" : ["tt0114709"]
            }
        }


class UpdateUserModel(BaseModel):
    userName: str
    email: Optional[EmailStr]
    password: Optional[str]
    genre : Optional[List[str]]
    filmsVue : Optional[List[str]]
    filmsPrefere :  Optional[List[str]]

    class Config:
        schema_extra = {
             "example": {
                "userName": "Jean",
                "email": "jean@jean.com"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}