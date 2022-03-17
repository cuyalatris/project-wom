from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Bienvenue"])
async def messageDeBienvenue():
    return { "message" : "Test projet wom"}