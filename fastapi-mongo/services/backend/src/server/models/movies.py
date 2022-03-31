from platform import release
import time
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field


class MovieSchema(BaseModel):
    id: str = Field(...)
    title: str = Field(...)
    fullTitle: str = Field(...)
    type: str = Field(...)
    year : str = Field(...)
    image : str = Field(...)
    releaseDate : str = Field(...)
    runtimeStr : str = Field(...)
    plot : str = Field(...)
    directors : str = Field(...)
    writers : str = Field(...)
    stars : str = Field(...)
    genres : str = Field(...)
    companies : str = Field(...)
    countries : str = Field(...)
    languages : str = Field(...)
    contentRating : str = Field(...)
    imDbRating : str = Field(...)
    tagline : str = Field(...)
    keywords : str = Field(...)
    similars : List[str] = Field(...)




    class Config:
        schema_extra = {
            "example": {
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
                "similars": ["tt0468569"]
                }
            }


class UpdateMoviesModel(BaseModel):
    id: str
    title: Optional[str]
    fullTitle: Optional[str]
    type: Optional[str]
    year : Optional[str]
    image : Optional[str]
    releaseDate : Optional[str]
    runtimeStr : Optional[str]
    plot : Optional[str]
    directors : Optional[str]
    writers : Optional[str]
    stars : Optional[str]
    genres : Optional[str]
    companies : Optional[str]
    countries : Optional[str]
    languages : Optional[str]
    contentRating : Optional[str]
    imDbRating : Optional[str]
    tagline : Optional[str]
    keywords : Optional[str]
    similars : Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
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
                "similars": ["tt0468569"]
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