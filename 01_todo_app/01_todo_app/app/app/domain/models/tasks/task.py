from pydantic import BaseModel, Field
from datetime import date

from app.domain.models.tasks.task_priority import TaskPriority
from app.domain.models.tasks.task_status import TaskStatus


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
