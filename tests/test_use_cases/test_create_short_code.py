from unittest import TestCase, mock
from app.use_cases import CreateShortCodeUseCase
from app.domain import UrlFactory
from tests import fixtures


class CreateShortCodeUseCaseTestCase(TestCase):

    def setUp(self):
        self.url1, self.url2 = fixtures.URL1, fixtures.URL2
        self.short_code_service = mock.Mock()
        self.short_code_service.create_code.return_value = "AAAA"
        self.repository = mock.Mock()
        self.factory = UrlFactory(self.short_code_service)
        self.use_case = CreateShortCodeUseCase(repo=self.repository,
                                               factory=self.factory)

    def test_instantiate(self):
        self.assertIsInstance(self.use_case, CreateShortCodeUseCase)

    def test_execute_returns_string(self):
        short_code = self.use_case.execute(self.url1)
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)

    def test_execute_calls_repository_save(self):
        url = self.factory.build(self.url1)
        short_code = self.use_case.execute(self.url1)
        self.repository.save.assert_called_once_with(url)
