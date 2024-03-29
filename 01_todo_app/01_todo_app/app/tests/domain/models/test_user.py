from app.domain.models.users.user_factory import UserFactory

from tests.tools.generator import ValueGenerator


class ユーザーを作成する場合:
    def 登録したパスワードで検証に成功すること(self):
        password = ValueGenerator.random_chara(10)
        sut = UserFactory.create(
            email=ValueGenerator.random_email(),
            name=ValueGenerator.random_chara(10),
            password=password,
        )

        assert sut.verify_password(password)


class ユーザー情報を変更する場合:
    def 変更したパスワードで検証に成功すること(self):
        password = ValueGenerator.random_chara(10)
        updated_password = ValueGenerator.random_chara(10)
        sut = UserFactory.create(
            email=ValueGenerator.random_email(),
            name=ValueGenerator.random_chara(10),
            password=password,
        )

        sut.update_password(password=updated_password)

        assert sut.verify_password(updated_password)

    def 変更前のパスワードで検証に失敗すること(self):
        password = ValueGenerator.random_chara(10)
        updated_password = ValueGenerator.random_chara(10)
        sut = UserFactory.create(
            email=ValueGenerator.random_email(),
            name=ValueGenerator.random_chara(10),
            password=password,
        )

        sut.update_password(password=updated_password)

        assert sut.verify_password(password) is False


class ユーザーのセッション情報を作成する場合:
    def 無効化期限は１時間であること(self):
        pass
