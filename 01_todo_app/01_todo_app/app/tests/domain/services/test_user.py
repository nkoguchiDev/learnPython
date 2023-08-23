from app.domain.models.users import UserFactory
from app.domain.services.user import UserService
from app.domain.repositories.user import IUserRepository
from app.infrastructure.mongodb.repositories.user import MongoUserRepository

from tests.tools.generator import ValueGenerator

user_repos: IUserRepository = MongoUserRepository()


class ユーザーが既に存在する場合:
    def ユーザードメインサービスはTrueを返すこと(self):
        user = UserFactory.create(
            email=ValueGenerator.random_email(),
            name=ValueGenerator.random_chara(10),
            password=ValueGenerator.random_chara(10),
        )
        user_repos.save(user)

        sut = UserService()

        assert sut.is_exist(user) is True


class ユーザーが存在しない場合:
    def ユーザードメインサービスはFalseを返すこと(self):
        user = UserFactory.create(
            email=ValueGenerator.random_email(),
            name=ValueGenerator.random_chara(10),
            password=ValueGenerator.random_chara(10),
        )

        sut = UserService()

        assert sut.is_exist(user) is False
