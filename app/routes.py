from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.use_cases import CreateShortCodeUseCase, GetShortCodeUseCase

router = APIRouter()

class RawUrl(BaseModel):
    url: str


@router.post("/")
async def create_short_code(body: RawUrl):
    use_case = CreateShortCodeUseCase()
    short_code = await use_case.execute(body.url)
    return {'short_code': short_code}

@router.get("/{short_code}")
async def get_short_code(short_code: str):
    use_case = GetShortCodeUseCase()
    url = await use_case.execute(short_code)
    return {'url': url.original}

@router.get("/{short_code}/stats/")
def get_short_code_stats(short_code: str):
    pass
