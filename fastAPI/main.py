from fastapi import FastAPI
from params import *

app = FastAPI()

@app.get("/", tags=["Bienvenue"])
async def messageDeBienvenue():
    return { "message" : "Bienvenue sur Nutflix !"}

@app.get('/getMovie/{title}')
async def researchByTitle(title):
    return {site + research_dico["SMovie"] + api_key + title}

@app.get('/getTopMovies')
async def researchByTitle():
    return {site + research_dico["TopMovies"] + api_key}