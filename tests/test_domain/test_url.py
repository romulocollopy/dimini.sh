from unittest import TestCase, mock
from app.domain import Url, UrlFactory
from tests import fixtures


class UrlTestCase(TestCase):

    def setUp(self):
        self.short_code_service = mock.Mock()
        self.factory = UrlFactory(self.short_code_service)

    def test_url1_build(self):
        url = self.factory.build(fixtures.URL1)
        self.assertIsInstance(url, Url)

    def test_url2_build(self):
        url = self.factory.build(fixtures.URL2)
        self.assertIsInstance(url, Url)
