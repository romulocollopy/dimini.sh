from app.repositories import UrlRepository


class GetShortCodeUseCase:

    def __init__(self, repo=None, factory=None):
        self.repo = repo or UrlRepository()

    async def execute(self, short_code: str) -> str:
        return await self.repo.get_by_short_code(short_code)
