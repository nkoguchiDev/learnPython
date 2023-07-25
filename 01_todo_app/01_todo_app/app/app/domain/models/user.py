from __future__ import annotations

from uuid import uuid4
from passlib.context import CryptContext

from pydantic import BaseModel, EmailStr, Field

from app.core.security import to_hashed_passowrd, verify_hashed_passowrd


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    id: str = Field(frozen=True)
    email: EmailStr
    hashed_password: str
    is_active: bool

    def verify_password(self, password) -> bool:
        return pwd_context.verify(password, self.hashed_password)

    def update_password(self, password) -> None:
        self.hashed_password = to_hashed_passowrd(password)


class UserFactory:
    @classmethod
    def create(cls, email: str, password: str) -> User:
        user_id = str(uuid4())
        hashed_password = pwd_context.hash(password)
        return User(
            id=user_id, email=email, hashed_password=hashed_password, is_active=True
        )
