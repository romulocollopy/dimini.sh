from urllib import parse
from pydantic import BaseModel


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

    @classmethod
    def build(cls, url_str: str):
        parsed = parse.urlparse(url_str)
        kwargs = parsed._asdict()
        kwargs["query"] = parse.parse_qs(kwargs["query"])
        inst = cls(original=url_str, **kwargs)
        inst.set_unparsed()
        return inst

    def _unparse(self) -> str:
        query = parse.urlencode(self.query, doseq=True)
        return parse.urlunparse(
            (
                self.scheme,
                self.netloc,
                self.path,
                self.params,
                query,
                self.fragment
            )
        )

    def set_unparsed(self) -> None:
        self.unparsed = self._unparse()
