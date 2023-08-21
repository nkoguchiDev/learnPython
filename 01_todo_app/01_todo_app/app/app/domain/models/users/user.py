from __future__ import annotations

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
