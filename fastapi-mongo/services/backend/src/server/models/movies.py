import time
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class MovieSchema(BaseModel):
    fullname: str = Field(...)
    genre: str = Field(...)
    director : str = Field(...)
    year: int = Field(..., gt=0, lt=2030)
    lienImage: str = Field(...)
    duree : str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Titanic",
                "genre": "Tragédie",
                "director": "Cameron",
                "year": 1958,
                "lienImage": "3.0",
                "duree": "2:30:00",
            }
        }


class UpdateMoviesModel(BaseModel):
    fullname: Optional[str]
    genre: Optional[str]
    director: Optional[str]
    year: Optional[int]
    lienImage: Optional[str]
    duree: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Titanic",
                "genre": "Tragédie",
                "director": "Cameron",
                "year": 1958,
                "lienImage": "3.0",
                "duree": "2:30:00",
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