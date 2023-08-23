from abc import abstractmethod

from app.domain.models.users import User
from app.domain.repositories.base import IRepository


class IUserRepository(IRepository[User]):
    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError()
