from freezegun import freeze_time
from unittest import mock, IsolatedAsyncioTestCase
from app.use_cases import CreateShortCodeUseCase
from app.domain import UrlFactory
from tests import fixtures


class CreateShortCodeUseCaseTestCase(IsolatedAsyncioTestCase):

    def setUp(self):
        self.url1, self.url2 = fixtures.URL1, fixtures.URL2
        self.short_code_service = mock.Mock()
        self.short_code_service.create_code = mock.Mock(return_value = "AAAA")
        self.repository = mock.AsyncMock()
        self.factory = UrlFactory(self.short_code_service)
        self.use_case = CreateShortCodeUseCase(repo=self.repository,
                                               factory=self.factory)

    async def test_instantiate(self):
        self.assertIsInstance(self.use_case, CreateShortCodeUseCase)

    async def test_execute_returns_string(self):
        short_code = await self.use_case.execute(self.url1)
        self.assertIsInstance(short_code, str)
        self.assertEqual(len(short_code), 4)

    @freeze_time("2020-10-03")
    async def test_execute_calls_repository_save(self):
        url = self.factory.build(self.url1)
        short_code = await self.use_case.execute(self.url1)
        self.repository.save.assert_called_once_with(url)
