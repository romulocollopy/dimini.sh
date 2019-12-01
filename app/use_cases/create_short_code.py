from app.domain import Url, UrlFactory
from app.repositories import UrlRepository


class CreateShortCodeUseCase:

    def __init__(self, repo=None, factory=None):
        self.repo = repo or UrlRepository()
        self.factory = factory or UrlFactory()

    def execute(self, raw_url: str) -> str:
        url = self.factory.build(raw_url)
        self.repo.save(url)
        return url.short_code
