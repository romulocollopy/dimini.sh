import logging

from app.repositories import UrlRepository

logger = logging.getLogger(__name__)


class GetShortCodeUseCase:
    def __init__(self, observers=None, repo=None):
        self.repo = repo or UrlRepository()
        self.observers = observers or []

    async def execute(self, short_code: str) -> str:
        url = await self.repo.get_by_short_code(short_code)
        await self.notify_observers(url)
        return url

    async def notify_observers(self, url, raises=False):
        try:
            for observer in self.observers:
                await observer.notify(url)
        except Exception as ex:
            logger.error(f"Observer error: ${ex.message}")
            if raises:
                raise ex
