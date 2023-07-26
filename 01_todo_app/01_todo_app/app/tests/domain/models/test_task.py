from datetime import date, timedelta

from app.domain.models.task import TaskFactory, TaskPriority, TaskStatus
from app.domain.events.task import TaskDeletedEvent


class タスクを作成する場合:
    def 作成したユーザに紐づいていること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )

        assert user.id == sut.userId


class タスク情報を変更する場合:
    def タイトルが変更できること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updated_title = "update"
        sut.update_title(title=updated_title)

        assert sut.title == updated_title

    def ステータスが変更できること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updatetd_status = TaskStatus.InProgress
        sut.update_status(status=updatetd_status)

        assert sut.status == updatetd_status

    def 期限日が変更できること(self, user):
        today = date.today()
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=today,
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updated_target_date = today + timedelta(days=1)
        sut.update_target_date(target_date=updated_target_date)

        assert sut.target_date == updated_target_date

    def 説明が変更できること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updated_description = "foo"
        sut.update_description(description=updated_description)

        assert sut.description == updated_description

    def 優先度が変更できること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )
        updated_priority = TaskPriority.High
        sut.update_priority(priority=updated_priority)

        assert sut.priority == updated_priority


class タスクを削除する場合:
    def タスク削除イベントが発行されること(self, user):
        sut = TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=date.today(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )

        sut.delete(user=user)

        assert TaskDeletedEvent(userId=user.id, taskId=sut.id) in sut.get_events()
