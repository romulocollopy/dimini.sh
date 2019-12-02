from unittest import TestCase, mock

from app.services import GenerateShortCodeService


class ShortCodeGeneratorServiceTestCase(TestCase):
    def setUp(self):
        self.service = GenerateShortCodeService()

    def test_create_code(self):
        code = self.service.create_code()
        self.assertIsInstance(code, str)
        self.assertEquals(len(code), 4)

    @mock.patch("app.services.short_code_generator.random_string_generator")
    def test_create_code(self, random_string):
        code = self.service.create_code()
        self.assertEquals(code, random_string())
