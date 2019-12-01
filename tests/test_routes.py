from app.repositories import UrlRepository
from tests.utils import APITestCase
from tests import fixtures


class RoutesTestCase(APITestCase):

    def test_create_short_code_route_configured(self):
        # TODO: this test could be better by mocking the use_case,
        # but in this function based approach of fastapi we would generate
        # unnecessary extra complexity
        resp = self.client.post("/", json={'url': fixtures.URL1})
        short_code = resp.json()['short_code']
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)

    def test_get_short_code_route_configured(self):
        resp = self.client.get("/AAAA")
        self.assertEqual(resp.json(), None)

    def test_get_short_code_stats_route_configured(self):
        resp = self.client.get("/AAAA/stats")
        self.assertEqual(resp.json(), None)
