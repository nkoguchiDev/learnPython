from uuid import uuid4
from enum import Enum, auto
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

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
    id: str = Field(frozen=True)
    userId: str
    title: str
    description: str
    target_date: date
    priority: TaskPriority
    status: TaskStatus

    def update_title(self, title: str) -> None:
        self.title = title

    def update_status(self, status: TaskStatus) -> None:
        self.status = status

    def update_target_date(self, target_date: date) -> None:
        self.target_date = target_date

    def update_description(self, description: str) -> None:
        self.description = description

    def update_priority(self, priority: TaskPriority) -> None:
        self.priority = priority


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
        task_id = str(uuid4())
        return Task(
            id=task_id,
            userId=user.id,
            title=title,
            description=description,
            target_date=target_date,
            priority=priority,
            status=status,
        )
