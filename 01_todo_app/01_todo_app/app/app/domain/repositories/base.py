from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from pydantic import BaseModel

DomainModelType = TypeVar("DomainModelType", bound=BaseModel)


class IRepository(ABC, Generic[DomainModelType]):
    @abstractmethod
    def get(self, id: str) -> DomainModelType | None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, entity: DomainModelType) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError()
