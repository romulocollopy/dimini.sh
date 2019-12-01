import unittest
import decouple
import asyncio
from app.repositories import UrlRepository
from app.domain import UrlFactory
from tests import fixtures

DATABASE_URL = decouple.config("TEST_DATABASE_URL")
DATABASE_NAME = decouple.config("TEST_DATABASE_NAME")


class UrlRepositoryTestCase(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        await UrlRepository.connect(DATABASE_URL, DATABASE_NAME)
        self.repo = UrlRepository()
        self.url = UrlFactory().build(fixtures.URL1)

    def test_instantiate(self):
        self.assertIsInstance(self.repo, UrlRepository)

    async def test_save(self):
        await self.repo.connect(DATABASE_URL, DATABASE_NAME)
        url_id = await self.repo.save(self.url)
        self.assertIsNotNone(url_id)

    async def test_connection(self):
        self.assertIsNotNone(self.repo._db)
        await UrlRepository.disconnect()
        self.assertIsNone(self.repo._db)

    async def asyncTearDown(self):
        await UrlRepository.disconnect()

