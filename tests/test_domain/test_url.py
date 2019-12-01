from unittest import TestCase
from app.domain import Url
from tests import fixtures


class UrlTestCase(TestCase):

    def test_url1_build(self):
        url = Url.build(fixtures.URL1)
        self.assertIsInstance(url, Url)

    def test_url2_build(self):
        url = Url.build(fixtures.URL2)
        self.assertIsInstance(url, Url)
