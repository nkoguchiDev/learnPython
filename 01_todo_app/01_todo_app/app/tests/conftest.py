import pytest
from mongoengine import connect, disconnect
from datetime import datetime

from app.core.config import settings
from app.domain.models.users import User, UserFactory
from app.domain.models.tasks import Task, TaskFactory, TaskPriority, TaskStatus

from app.infrastructure.mongodb.repositories.user import Schema as UserDB

from tests.tools.generator import ValueGenerator


@pytest.fixture(scope="function")
def user() -> User:
    return UserFactory.create(
        email=ValueGenerator.random_email(),
        name=ValueGenerator.random_chara(10),
        password=ValueGenerator.random_chara(10),
    )


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
def mongodb_connect():
    connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        uuidRepresentation="standard",
        alias=settings.PROJECT_NAME,
    )
    yield
    UserDB().drop_collection()
    disconnect(alias=settings.PROJECT_NAME)
