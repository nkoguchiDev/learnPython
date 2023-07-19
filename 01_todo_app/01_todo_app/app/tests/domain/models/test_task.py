from uuid import uuid4

from app.domain.models.user import User
from app.domain.models.task import Task, TaskPriority


class タスクを作成する場合:
    def 作成したユーザの空間に指定した名前で作成されること(self):
        user_id = str(uuid4())
        user_name = "username"
        user = User(id=user_id, name=user_name)

        task_title="title"
        task_description="description"
        task = user.create_task(title, description, targetDate, priority)

        assert task == Task(
            id=task.id,
            userId=user.id,
            title=title,
            description=description,
            targetDate=task.targetDate,
            priority=TaskPriority.Middle,
        )
