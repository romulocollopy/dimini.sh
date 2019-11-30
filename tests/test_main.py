from unittest import TestCase
from starlette.testclient import TestClient
from main import app


client = TestClient(app)


class MainTestCase(TestCase):

    def test_get_home(self):
        resp = client.get("/")
        self.assertEqual(resp.json(), {'message': 'Welcome to dimini.sh'})
