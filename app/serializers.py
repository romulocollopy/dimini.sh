from datetime import datetime

from pydantic import BaseModel


class BaseSerializer(BaseModel):
    @classmethod
    def serialize(cls, obj: dict):
        instance = cls(**obj)
        return instance.dict()


class RawUrl(BaseSerializer):
    url: str


class ShortCodeSerializer(BaseSerializer):
    short_code: str


class OriginalUrlSerializer(BaseSerializer):
    url: str


class StatsSerializer(BaseSerializer):
    url: str
    creationDate: datetime
    accessCount: int
