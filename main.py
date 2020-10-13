import decouple
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.repositories import UrlRepository
from app.routes import router

app = FastAPI()

DATABASE_URL = decouple.config("TEST_DATABASE_URL")
DATABASE_NAME = decouple.config("TEST_DATABASE_NAME")


@app.get("/")
def home():
    return RedirectResponse("/ui/", status_code=301)


@app.on_event("startup")
async def setup_db():
    await UrlRepository.connect(DATABASE_URL, DATABASE_NAME)


@app.on_event("shutdown")
async def shutdown():
    await UrlRepository.disconnect()


app.include_router(router)
