import decouple
from unittest import IsolatedAsyncioTestCase

from starlette.testclient import TestClient
from main import app

from tests import fixtures
from app.repositories import UrlRepository
from app.domain import Url

DATABASE_URL = decouple.config("TEST_DATABASE_URL")
DATABASE_NAME = decouple.config("TEST_DATABASE_NAME")


class RoutesTestCase(IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        await UrlRepository.connect(DATABASE_URL, DATABASE_NAME)
        repo = UrlRepository()
        url = Url(**{
            'scheme': '',
            'netloc': '',
            'path': '',
            'params': '',
            'query': {},
            'fragment': '',
            'original': fixtures.URL1,
            'unparsed': fixtures.URL1,
            'short_code': 'AAAA'}
        )
        url2 = Url(**{
            'scheme': '',
            'netloc': '',
            'path': '',
            'params': '',
            'query': {},
            'fragment': '',
            'original': fixtures.URL1,
            'unparsed': fixtures.URL1,
            'access_count': 593,
            'short_code': 'BBBB'}
        )
        await repo.save(url)
        await repo.save(url2)

    def test_create_short_code_route_configured(self):
        # TODO: this test could be better by mocking the use_case,
        # but in this function based approach of fastapi we would generate
        # unnecessary extra complexity
        with TestClient(app) as client:
            resp = client.post("/", json={'url': fixtures.URL1})
        short_code = resp.json()['short_code']
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)

    def test_get_short_code_route_configured(self):
        with TestClient(app) as client:
            resp = client.get("/AAAA")
        self.assertEqual(resp.json()["url"], fixtures.URL1)

    def test_get_short_code_stats_route_configured(self):
        with TestClient(app) as client:
            resp = client.get("/BBBB/stats")
        self.assertEqual(resp.json()["accessCount"], 593)

    def test_get_home(self):
        with TestClient(app) as client:
            resp = client.get("/")
        self.assertEqual(resp.json(), {'message': 'Welcome to dimini.sh'})
