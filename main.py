from fastapi import FastAPI
import decouple
from app.routes import router
from app.repositories import UrlRepository
app = FastAPI()

DATABASE_URL = decouple.config("TEST_DATABASE_URL")
DATABASE_NAME = decouple.config("TEST_DATABASE_NAME")


@app.get("/")
def home():
    return {"message": "Welcome to dimini.sh"}


@app.on_event("startup")
async def setup_db():
    await UrlRepository.connect(DATABASE_URL, DATABASE_NAME)


app.include_router(router)
