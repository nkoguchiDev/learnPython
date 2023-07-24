from datetime import datetime

from app.domain.models.user import UserFactory
from app.domain.models.task import TaskFactory, TaskPriority, TaskStatus


class タスクを作成する場合:
    def 作成したユーザに紐づいていること(self, user):
        task = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            targetDate=datetime.now(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )

        assert user.id == task.userId


class タスク情報を変更する場合:
    def タイトルが変更できること(self, user):
        task = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            targetDate=datetime.now(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updated_title = "update"
        task.update_title(title=updated_title)

        assert task.title == updated_title

    def ステータスが変更できること(self, user):
        task = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            targetDate=datetime.now(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updatetd_status = TaskStatus.InProgress
        task.update_status(status=updatetd_status)

        assert task.status == updatetd_status

    def 期限日が変更できること(self):
        pass

    def 説明が変更できること(self):
        pass

    def 優先度が変更できること(self):
        pass
