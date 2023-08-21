from enum import Enum, auto


class TaskStatus(Enum):
    Todo = auto()
    InProgress = auto()
    Done = auto()
