from unittest import TestCase
from app.domain import Url
from tests import fixtures


class UrlTestCase(TestCase):

    def test_url1_parse(self):
        Url.parse(fixtures.URL1)

    def test_url2_parse(self):
        Url.parse(fixtures.URL2)

    def test_url1_unparse(self):
        url = Url.parse(fixtures.URL1)
        url.unparse()

    def test_url2_unparse(self):
        url = Url.parse(fixtures.URL2)
        url.unparse()

