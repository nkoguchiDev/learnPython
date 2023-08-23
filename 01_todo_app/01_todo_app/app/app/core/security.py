from passlib.context import CryptContext


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def to_hashed_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password, password_hash: str) -> bool:
        return cls.pwd_context.verify(password, password_hash)
