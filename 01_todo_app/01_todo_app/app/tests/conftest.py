import pytest

from datetime import datetime

from app.infrastructure.database.connection import db
from app.domain.models.user import User, UserFactory
from app.domain.models.task import Task, TaskFactory, TaskPriority, TaskStatus


@pytest.fixture(scope="function")
def user() -> User:
    return UserFactory.create(email="test@email.co.jp", password="password")


@pytest.fixture(scope="function")
def task() -> Task:
    def excute(user: User):
        return TaskFactory.create(
            user=user,
            title="title",
            description="hi",
            target_date=datetime.now(),
            priority=TaskPriority.Middle,
            status=TaskStatus.Todo,
        )

    return excute


@pytest.fixture(scope="class", autouse=True)
def scope_class():
    yield
    db.command("dropDatabase")
