from fastapi import APIRouter, Body
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED
from app.use_cases import CreateShortCodeUseCase, GetShortCodeUseCase
from app.observers import AccessCountObserver
from app.repositories.url import ShortCodeNotFound

router = APIRouter()

class RawUrl(BaseModel):
    url: str


@router.post("/")
async def create_short_code(body: RawUrl):
    use_case = CreateShortCodeUseCase()
    short_code = await use_case.execute(body.url)
    return JSONResponse(status_code=HTTP_201_CREATED,
                        content={'short_code': short_code})

@router.get("/{short_code}")
async def get_short_code(short_code: str):
    observers = [AccessCountObserver()]
    use_case = GetShortCodeUseCase(observers=observers)
    try:
        url = await use_case.execute(short_code)
    except ShortCodeNotFound:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'reason': "Not Found"})

    return {'url': url.original}

@router.get("/{short_code}/stats/")
async def get_short_code_stats(short_code: str):
    use_case = GetShortCodeUseCase()
    try:
        url = await use_case.execute(short_code)
    except ShortCodeNotFound:
        return {'reason': "Not Found"}

    return {
        'url': url.original,
        'creation_date': url,
        'accessCount': url.access_count,
    }
