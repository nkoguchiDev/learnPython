import pytest

from app.domain.services.user import UserService
from app.domain.repositories.user import IUserRepository
from app.infrastructure.mongodb.repositories.user import MongoUserRepository
from app.application.services.user import UserApplicationService

from app.errors.user import DuplicateUserException

from tests.tools.generator import ValueGenerator

user_service: UserService = UserService()
user_repos: IUserRepository = MongoUserRepository()


class アプリケーションでユーザーを作成する場合:
    def データが永続化されること(self):
        user_email = ValueGenerator.random_email()
        sut = UserApplicationService(
            user_service=user_service, user_repository=user_repos
        )

        sut.register(
            name=ValueGenerator.random_chara(10),
            email=user_email,
            password=ValueGenerator.random_chara(10),
        )

        assert user_repos.get_by_email(email=user_email)

    def 同一emailのユーザーがいる場合は作成に失敗すること(self, user):
        user_repos.save(user)
        sut = UserApplicationService(
            user_service=user_service, user_repository=user_repos
        )

        with pytest.raises(DuplicateUserException):
            sut.register(
                name=user.name,
                email=user.email,
                password=ValueGenerator.random_chara(10),
            )
