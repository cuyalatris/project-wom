from fastapi import FastAPI

from src.server.routes.movie import router as MovieRouter

app = FastAPI()

app.include_router(MovieRouter, tags=["Movie"], prefix="/movie")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
