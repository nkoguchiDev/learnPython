from uuid import uuid4

from app.domain.models.user import User
from app.domain.models.task import Task, TaskPriority


class タスクを作成する場合:
    def 作成したユーザに紐づいていること(self):
        pass


class タスク情報を変更する場合:
    def タイトルが変更できること(self):
        pass

    def ステータスが変更できること(self):
        pass

    def 期限日が変更できること(self):
        pass

    def 説明が変更できること(self):
        pass
