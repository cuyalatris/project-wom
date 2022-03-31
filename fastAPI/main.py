from asyncio.base_subprocess import ReadSubprocessPipeProto
from urllib import response
from fastapi import FastAPI
import requests
from params import *
import json
app = FastAPI()

@app.get("/", tags=["Bienvenue"])
async def messageDeBienvenue():
    return { "message" : "Bienvenue sur Nutflix !"}

@app.get('/Movies/SearchMovie/{title}')
async def researchByTitle(title):
    response = requests.get(site + research_dico["SMovie"] + api_key + title).json()
    return response

@app.get('/Movies/GetTop250Movies')
async def researchTop250():
    response = requests.get(site + research_dico["TopMovies"] + api_key).json()
    return response

@app.get('/Movies/GetMostPopular')
async def researchMostPop():
    response = requests.get(site + research_dico["MostPopMovies"] + api_key).json()
    return response

@app.get('/All/SearchInAll/{expression}')
async def researchAll(expression):
    response = requests.get(site + research_dico["SAll"] + api_key + expression).json()
    return response

@app.get('/Movies/GetInfos/{id}')
async def getInfos(id):
    print(site + research_dico["STitle"] + api_key + id + option)
    response = requests.get(site + research_dico["STitle"] + api_key + id + option).json()
    return response