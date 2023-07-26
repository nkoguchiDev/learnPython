from __future__ import annotations
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field

from app.core.security import Password


class User(BaseModel):
    id: str = Field(frozen=True)
    email: EmailStr
    hashed_password: str
    is_active: bool

    def verify_password(self, password) -> bool:
        return Password.verify_password(password, self.hashed_password)

    def update_password(self, password) -> None:
        self.hashed_password = Password.to_hashed_password(password)


class UserFactory:
    @classmethod
    def create(cls, email: str, password: str) -> User:
        return User(
            id=str(uuid4()),
            email=email,
            hashed_password=Password.to_hashed_password(password),
            is_active=True,
        )
