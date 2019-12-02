from datetime import datetime
from urllib import parse

from pydantic import BaseModel

from app.services import GenerateShortCodeService


class Url(BaseModel):
    scheme: str
    netloc: str
    path: str
    params: str
    query: dict
    fragment: str
    original: str
    unparsed: str = None
    short_code: str = None
    access_count: int = 0
    created_at: datetime = None

    def __init__(self, short_code_service=None, **kwargs):
        super().__init__(**kwargs)
        self.created_at = datetime.now()
        self.set_unparsed()
        if not self.short_code:
            self.short_code = self._generate_short_code(short_code_service)

    def _unparse(self) -> str:
        query = parse.urlencode(self.query, doseq=True)
        return parse.urlunparse(
            (self.scheme, self.netloc, self.path, self.params, query, self.fragment)
        )

    def set_unparsed(self) -> None:
        self.unparsed = self._unparse()

    @staticmethod
    def _generate_short_code(short_code_service):
        return short_code_service.create_code()


class UrlFactory:
    def __init__(self, short_code_service=None) -> None:
        self.short_code_service = short_code_service or GenerateShortCodeService()

    def build(self, url_str: str) -> Url:
        parsed = parse.urlparse(url_str)
        kwargs = parsed._asdict()
        kwargs["original"] = url_str
        kwargs["query"] = parse.parse_qs(kwargs["query"])
        return Url(short_code_service=self.short_code_service, **kwargs)
