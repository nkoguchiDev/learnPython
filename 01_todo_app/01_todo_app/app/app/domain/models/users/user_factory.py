from uuid import uuid4

from app.domain.models.users.user import User
from app.core.security import Password


class UserFactory:
    @classmethod
    def create(cls, email: str, password: str) -> User:
        return User(
            id=str(uuid4()),
            email=email,
            hashed_password=Password.to_hashed_password(password),
            is_active=True,
        )
