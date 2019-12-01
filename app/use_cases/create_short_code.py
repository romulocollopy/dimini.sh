from app.services import GenerateShortCodeService
from app.domain import Url


class CreateShortCodeUseCase:

    def __init__(self, code_generator=None):
        self.service = code_generator or GenerateShortCodeService()

    def execute(self, url: str) -> str:
        url = Url.build(url)
        short_code = self.service.create_code()
        url.short_code = short_code
        return short_code
