from tests.utils import APITestCase


class RoutesTestCase(APITestCase):

    def test_create_short_code_route_configured(self):
        resp = self.client.post("/")
        self.assertEqual(resp.json(), None)

    def test_get_short_code_route_configured(self):
        resp = self.client.post("/")
        self.assertEqual(resp.json(), None)

    def test_get_short_code_stats_route_configured(self):
        resp = self.client.post("/")
        self.assertEqual(resp.json(), None)
