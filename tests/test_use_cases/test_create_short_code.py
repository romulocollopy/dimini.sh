from unittest import TestCase, mock
from app.use_cases import CreateShortCodeUseCase

URL1 = (
    "https://www.openstreetmap.org/search?whereami=1&"
    "query=-22.93396%2C-43.18033#map=19/-22.93396/-43.18033"
)

URL2 = (
    "https://www.basic-fit.com/nl-nl/sportschool/"
    "basic-fit-amsterdam-wfc-1bd19ff0981849b19081bbf0f20e1ac2.html"
    "?utm_source=google&utm_medium=organic&utm_content=gmb&"
    "utm_campaign=localmaps"
)


class CreateShortCodeUseCaseTestCase(TestCase):

    def setUp(self):
        self.url1, self.url2 = URL1, URL2
        self.short_code_service = mock.Mock()
        self.short_code_service.create_code = mock.Mock(return_value="AAAA")
        self.use_case = CreateShortCodeUseCase(self.short_code_service)

    def test_instantiate(self):
        self.assertIsInstance(self.use_case, CreateShortCodeUseCase)

    def test_execute_returns_string(self):
        short_code = self.use_case.execute(self.url1)
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)
