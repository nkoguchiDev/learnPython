from uuid import uuid4
from datetime import date

from app.domain.models.users import User
from app.domain.models.tasks import Task, TaskPriority, TaskStatus


class TaskFactory:
    @classmethod
    def create(
        cls,
        user: User,
        title: str,
        description: str,
        target_date: date,
        priority: TaskPriority,
        status: TaskStatus,
    ):
        return Task(
            id=str(uuid4()),
            userId=user.id,
            title=title,
            description=description,
            target_date=target_date,
            priority=priority,
            status=status,
        )
