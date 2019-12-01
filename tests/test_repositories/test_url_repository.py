import unittest
import decouple
from app.repositories import UrlRepository
from app.domain import UrlFactory, Url
from tests import fixtures

DATABASE_URL = decouple.config("TEST_DATABASE_URL")
DATABASE_NAME = decouple.config("TEST_DATABASE_NAME")


class UrlRepositoryTestCase(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        await UrlRepository.connect(DATABASE_URL, DATABASE_NAME)
        self.repo = UrlRepository()
        self.short_url = "AAAA"
        short_code_service = unittest.mock.Mock()
        short_code_service.create_code.return_value = self.short_url
        self.url = UrlFactory(short_code_service).build(fixtures.URL1)

    def test_instantiate(self):
        self.assertIsInstance(self.repo, UrlRepository)

    async def test_save(self):
        url_id = await self.repo.save(self.url)
        self.assertIsNotNone(url_id)

    async def test_get_by_short_url(self):
        await self.repo.save(self.url)
        url = await self.repo.get_by_short_code(self.short_url)
        self.assertIsInstance(url, Url)

    async def test_connection(self):
        self.assertIsNotNone(self.repo._db)
        await UrlRepository.disconnect()
        self.assertIsNone(self.repo._db)

    async def asyncTearDown(self):
        self.repo.collection.delete_many({})
        await UrlRepository.disconnect()
