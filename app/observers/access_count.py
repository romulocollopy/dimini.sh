from app.repositories import UrlRepository


class AccessCountObserver:
    def __init__(self, repo=None):
        self.repo = repo or UrlRepository()

    async def notify(self, url):
        await self.repo.increment_access_count(url)
