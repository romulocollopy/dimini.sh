from fastapi import APIRouter, Body
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.observers import AccessCountObserver
from app.repositories.url import ShortCodeNotFound
from app.serializers import (OriginalUrlSerializer, RawUrl,
                             ShortCodeSerializer, StatsSerializer)
from app.use_cases import CreateShortCodeUseCase, GetShortCodeUseCase

router = APIRouter()


@router.post("/")
async def create_short_code(body: RawUrl):
    use_case = CreateShortCodeUseCase()
    short_code = await use_case.execute(body.url)
    return JSONResponse(
        status_code=HTTP_201_CREATED,
        content=ShortCodeSerializer.serialize({"short_code": short_code}),
    )


@router.get("/{short_code}")
async def get_short_code(short_code: str):
    observers = [AccessCountObserver()]
    use_case = GetShortCodeUseCase(observers=observers)
    try:
        url = await use_case.execute(short_code)
    except ShortCodeNotFound:
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND, content={"reason": "Not Found"}
        )

    return OriginalUrlSerializer.serialize({"url": url.original})


@router.get("/{short_code}/stats/")
async def get_short_code_stats(short_code: str):
    use_case = GetShortCodeUseCase()
    try:
        url = await use_case.execute(short_code)
    except ShortCodeNotFound:
        return {"reason": "Not Found"}

    return StatsSerializer.serialize(
        {
            "url": url.original,
            "creationDate": url.created_at,
            "accessCount": url.access_count,
        }
    )
