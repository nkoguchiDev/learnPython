from app.domain.models.user import User
from app.infrastructure.database.connection import db


class UserRepository:
    def __init__(self) -> None:
        self._database = db.users

    def get_by_email(self, email: str) -> User | None:
        user_data = self._database.find_one({"email": email})
        if user_data is None:
            return None
        return User(**user_data)

    def save(self, user: User) -> None:
        self._database.replace_one({"id": user.id}, user.model_dump(), upsert=True)
