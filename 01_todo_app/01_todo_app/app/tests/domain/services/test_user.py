from app.domain.models.user import User, UserFactory
from app.domain.services.user import UserService
from app.domain.repositories.user import UserRepository


def create_user(email: str, password: str) -> User:
    user = UserFactory.create(email=email, password=password)
    userRepository = UserRepository()
    userRepository.save(user)
    return user


class ユーザーが既に存在する場合:
    def ユーザードメインサービスはTrueを返すこと(self):
        user = create_user(email="email@test.com", password="password")
        sut = UserService()
        assert sut.is_exist(email=user.email) is True


class ユーザーが存在しない場合:
    def ユーザードメインサービスはFalseを返すこと(self):
        user = UserFactory.create(email="email@noexist.user.com", password="password")
        sut = UserService()
        assert sut.is_exist(email=user.email) is False
