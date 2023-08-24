from app.domain.models.users.user_factory import UserFactory
from app.domain.services.user import UserService
from app.domain.repositories.user import IUserRepository

from app.errors.user import DuplicateUserException


class UserApplicationService:
    def __init__(
        self, user_service: UserService, user_repository: IUserRepository
    ) -> None:
        self.__user_service = user_service
        self.__user_repository = user_repository

    def register(self, name: str, email: str, password: str) -> None:
        user = UserFactory.create(name=name, email=email, password=password)

        if self.__user_service.is_exist(user):
            raise DuplicateUserException()

        self.__user_repository.save(user)
