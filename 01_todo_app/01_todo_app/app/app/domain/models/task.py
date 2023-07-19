from enum import Enum, auto
from pydantic import BaseModel
from datetime import datetime


class TaskPriority(Enum):
    High = auto()
    Middle = auto()
    Low = auto()


class TaskStatus(Enum):
    Draft = auto()
    Todo = auto()
    Done = auto()


class Task(BaseModel):
    id: str
    userId: str
    title: str
    description: str
    targetDate: datetime
    priority: TaskPriority
    status: TaskStatus
