from unittest import mock, IsolatedAsyncioTestCase
from app.use_cases import GetShortCodeUseCase
from app.domain import UrlFactory
from tests import fixtures


class GetShortCodeUseCaseTestCase(IsolatedAsyncioTestCase):

    def setUp(self):
        self.url1 = fixtures.URL1
        self.repository = mock.AsyncMock()
        self.repository.get_by_short_code.return_value = self.url1
        self.use_case = GetShortCodeUseCase(repo=self.repository)

    async def test_instantiate(self):
        self.assertIsInstance(self.use_case, GetShortCodeUseCase)

    async def test_execute_returns_string(self):
        short_code = "AAAA"
        url = await self.use_case.execute(short_code)
        self.assertEqual(url, fixtures.URL1)

    async def test_execute_calls_repository_get_by_short_code(self):
        short_code = "AAAA"
        url = await self.use_case.execute(short_code)
        self.repository.get_by_short_code.assert_called_once_with(short_code)
