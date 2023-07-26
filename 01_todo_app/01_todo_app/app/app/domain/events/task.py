from app.domain.events.base import DomainEvent


class TaskDomainEvent(DomainEvent):
    userId: str
    taskId: str


class TaskDeletedEvent(TaskDomainEvent):
    ...
