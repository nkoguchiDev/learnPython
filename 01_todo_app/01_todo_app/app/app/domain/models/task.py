from uuid import uuid4
from enum import Enum, auto
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from app.domain.models.user import User


class TaskPriority(Enum):
    High = auto()
    Middle = auto()
    Low = auto()


class TaskStatus(Enum):
    Todo = auto()
    InProgress = auto()
    Done = auto()


class Task(BaseModel):
    id: str
    userId: str
    title: str
    description: str
    targetDate: datetime
    priority: TaskPriority
    status: TaskStatus

    def update_title(self, title: str) -> None:
        self.title = title

    def update_status(self, status: TaskStatus) -> None:
        self.status = status


class TaskFactory:
    @classmethod
    def create(
        cls,
        user: User,
        title: str,
        description: str,
        targetDate: datetime,
        priority: TaskPriority,
        status: TaskStatus,
    ):
        task_id = str(uuid4())
        return Task(
            id=task_id,
            userId=user.id,
            title=title,
            description=description,
            targetDate=targetDate,
            priority=priority,
            status=status,
        )
