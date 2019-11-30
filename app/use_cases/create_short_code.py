from app.services import GenerateShortCodeService


class CreateShortCodeUseCase:

    def __init__(self, code_generator=None):
        self.service = code_generator or GenerateShortCodeService()

    def execute(self, url: str) -> str:
        return self.service.create_code()
