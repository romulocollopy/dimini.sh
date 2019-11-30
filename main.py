from fastapi import FastAPI
from app.routes import router
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to dimini.sh"}

app.include_router(router)
