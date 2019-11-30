from unittest import TestCase, mock
from app.use_cases import CreateShortCodeUseCase
from tests import fixtures


class CreateShortCodeUseCaseTestCase(TestCase):

    def setUp(self):
        self.url1, self.url2 = fixtures.URL1, fixtures.URL2
        self.short_code_service = mock.Mock()
        self.short_code_service.create_code = mock.Mock(return_value="AAAA")
        self.use_case = CreateShortCodeUseCase(self.short_code_service)

    def test_instantiate(self):
        self.assertIsInstance(self.use_case, CreateShortCodeUseCase)

    def test_execute_returns_string(self):
        short_code = self.use_case.execute(self.url1)
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)
