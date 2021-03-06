import motor.motor_asyncio

from app.domain import Url


class ShortCodeNotFound(Exception):
    pass


class UrlRepository:
    COLLECTION_NAME = "url_collection"
    _db = None
    collection = None

    async def save(self, url: Url) -> str:
        ormUrl = self.to_orm(url)
        result = await self.collection.insert_one(ormUrl)
        return result.inserted_id

    async def increment_access_count(self, url: Url) -> str:
        result = await self.collection.update_one(
            {"short_code": url.short_code}, {"$inc": {"access_count": 1}}
        )

    async def get_by_short_code(self, short_code: str) -> str:
        url = await self.collection.find_one({"short_code": short_code})
        if not url:
            raise ShortCodeNotFound()
        return await self.to_domain(url)

    @classmethod
    async def connect(cls, database_url: str, database_name: str) -> None:
        if cls._db and cls.collection:
            return

        client = motor.motor_asyncio.AsyncIOMotorClient(database_url)
        cls._db = getattr(client, database_name)
        cls.collection = getattr(cls._db, cls.COLLECTION_NAME)

    @classmethod
    async def disconnect(cls) -> None:
        cls._db = None
        cls._collection = None

    @staticmethod
    def to_orm(url):
        return dict(url)

    async def to_domain(self, url: dict) -> Url:
        return Url(**url)
