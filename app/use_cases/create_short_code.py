from app.domain import UrlFactory
from app.repositories import UrlRepository


class CreateShortCodeUseCase:
    def __init__(self, repo=None, factory=None):
        self.repo = repo or UrlRepository()
        self.factory = factory or UrlFactory()

    async def execute(self, raw_url: str) -> str:
        url = self.factory.build(raw_url)
        await self.repo.save(url)
        return url.short_code
