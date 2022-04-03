from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.server.routes.movie import router as MovieRouter
from src.server.routes.user import router as UserRouter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://0.0.0.0:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

app.include_router(MovieRouter, tags=["Movie"], prefix="/movie")

app.include_router(UserRouter, tags=["User"], prefix="/user")






