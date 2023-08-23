from mongoengine import Document
from mongoengine.fields import StringField

from app.domain.models.users.user import User
from app.domain.repositories.user import IUserRepository
from app.core.config import settings


class Schema(Document):
    id_ = StringField(required=True, db_field="id")
    email = StringField(required=True)
    name = StringField(required=True)
    password_hash = StringField(required=True)

    meta = {
        "db_alias": settings.DB_NAME,
        "collection": "users",
    }


class MongoUserRepository(IUserRepository):
    def get(self, id: str) -> User | None:
        user = Schema.objects(id_=id).first()

        if user is None:
            return None

        return User(
            id=user.id,
            name=user.name,
            email=user.email,
            password_hash=user.password_hash,
        )

    def save(self, entity: User) -> None:
        Schema(
            id_=entity.id,
            email=entity.email,
            name=entity.name,
            password_hash=entity.password_hash,
        ).save()

    def delete(self, id: str) -> None:
        Schema.objects(id_=id).first().delete()

    def get_by_email(self, email: str) -> User | None:
        user = Schema.objects(email=email).first()

        if user is None:
            return None

        return User(
            id=user.id,
            name=user.name,
            email=user.email,
            password_hash=user.password_hash,
        )
