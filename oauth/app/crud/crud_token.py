import redis

from app.core.config import settings
from app.schema.crud import Token
from app.libs.converter import ModelConverter


class CRUDToken:
    def __init__(self) -> None:
        pass

    def create(
            self,
            cache: redis,
            key: str,
            data: dict) -> list:
        return cache.hset(key, mapping=Token(**data).dict(exclude_none=True))

    def get(
            self,
            cache: redis,
            key: str) -> list:
        return ModelConverter.byte_key_value_to_dict(cache.hgetall(key))

    def delete(
            self,
            cache: redis,
            key: str) -> list:
        return cache.delete(key)


token = CRUDToken()
