from unittest import TestCase
from starlette.testclient import TestClient
from main import app


class APITestCase(TestCase):

    def __init__(self, *args, **kwargs):
        self.client = kwargs.pop('client', None) or TestClient(app)
        super().__init__(*args, **kwargs)
