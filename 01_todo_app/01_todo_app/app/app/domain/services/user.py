from app.domain.models.users.user import User
from app.domain.repositories.user import IUserRepository
from app.infrastructure.mongodb.repositories.user import MongoUserRepository


class UserService:
    def __init__(self) -> None:
        self._user_repos: IUserRepository = MongoUserRepository()

    def is_exist(self, user: User) -> bool:
        return self._user_repos.get_by_email(email=user.email) is not None
