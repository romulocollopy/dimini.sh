from app.domain import Url
import motor.motor_asyncio


class UrlRepository:
    COLLECTION_NAME = "url_collection"
    _db = None
    collection = None

    async def save(self, url: Url) -> None:
        ormUrl = self.to_orm(url)
        result = await self.collection.insert_one(ormUrl)
        return result.inserted_id

    @classmethod
    async def connect(cls, database_url: str, database_name: str, io_loop=None) -> None:
        if cls._db and cls.collection:
            return

        kwargs = {}
        if io_loop:
            kwargs['io_loop'] = io_loop

        client = motor.motor_asyncio.AsyncIOMotorClient(
            database_url, **kwargs
        )
        cls._db = getattr(client, database_name)
        cls.collection = getattr(cls._db, cls.COLLECTION_NAME)

    @classmethod
    async def disconnect(cls) -> None:
        cls._db = None
        cls._collection = None

    @staticmethod
    def to_orm(url):
        return dict(url)
