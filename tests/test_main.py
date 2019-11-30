from tests.utils import APITestCase


class MainTestCase(APITestCase):

    def test_get_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.json(), {'message': 'Welcome to dimini.sh'})
