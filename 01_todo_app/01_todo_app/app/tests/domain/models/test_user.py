from uuid import uuid4

from app.domain.models.user import User


class ユーザーを作成する場合:
    def 登録したパスワードで検証に成功すること(self):
        password = "password"
        sut = User.create(email="test@email.co.jp", password=password)

        assert sut.verify_password(password)
