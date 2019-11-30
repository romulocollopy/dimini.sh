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

    @classmethod
    def parse(cls, url_str):
        parsed = parse.urlparse(url_str)
        kwargs = parsed._asdict()
        kwargs["query"] = parse.parse_qs(kwargs["query"])
        return cls(original=url_str, **kwargs)

    def unparse(self):
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

