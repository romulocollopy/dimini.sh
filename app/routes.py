from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create_short_code():
    pass

@router.get("{short_code}")
def get_short_code(short_code: str):
    pass

@router.get("{short_code}/stats/")
def get_short_code_stats(short_code: str):
    pass
