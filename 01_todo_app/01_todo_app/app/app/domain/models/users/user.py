from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field

from app.core.security import Password


class User(BaseModel):
    id: str = Field(frozen=True)
    name: str
    email: EmailStr
    password_hash: str

    def verify_password(self, password) -> bool:
        return Password.verify_password(password, self.password_hash)

    def update_password(self, password) -> None:
        self.password_hash = Password.to_hashed_password(password)
