from app.domain.models.user import UserFactory


class ユーザーを作成する場合:
    def 登録したパスワードで検証に成功すること(self):
        password = "password"
        sut = UserFactory.create(email="test@email.co.jp", password=password)

        assert sut.verify_password(password)


class ユーザー情報を変更する場合:
    def 変更したパスワードで検証に成功すること(self):
        password = "password"
        sut = UserFactory.create(email="test@email.co.jp", password=password)

        assert sut.verify_password(password)
