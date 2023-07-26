from passlib.context import CryptContext


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def to_hashed_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password, hashed_password: str) -> bool:
        return cls.pwd_context.verify(password, hashed_password)
