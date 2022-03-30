import time
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    userName: str = Field(...)
    email: EmailStr = Field(...)
    password : str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "userName": "Pierre",
                "email": "pierre@pierre.com",
                "password": "PeterPan4",
            }
        }


class UpdateUserModel(BaseModel):
    userName: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        schema_extra = {
             "example": {
                "userName": "Pierre",
                "email": "pierre@pierre.com",
                "password": "PeterPan4",
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