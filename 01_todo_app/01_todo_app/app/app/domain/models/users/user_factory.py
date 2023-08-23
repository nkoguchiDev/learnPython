from uuid import uuid4

from app.domain.models.users.user import User
from app.core.security import Password


class UserFactory:
    @classmethod
    def create(cls, email: str, name: str, password: str) -> User:
        return User(
            id=str(uuid4()),
            email=email,
            name=name,
            password_hash=Password.to_hashed_password(password),
        )
