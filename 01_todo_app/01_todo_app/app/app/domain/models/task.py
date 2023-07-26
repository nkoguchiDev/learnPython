from uuid import uuid4
from enum import Enum, auto
from typing import List
from pydantic import BaseModel, Field
from datetime import date

from app.domain.models.user import User
from app.domain.events.task import TaskDomainEvent, TaskDeletedEvent


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

    events: List[TaskDomainEvent] = Field(default=[], exclude=True)

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

    def delete(self, user: User) -> None:
        self.events.append(TaskDeletedEvent(userId=user.id, taskId=self.id))

    def get_events(self) -> List[TaskDomainEvent]:
        return self.events


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
