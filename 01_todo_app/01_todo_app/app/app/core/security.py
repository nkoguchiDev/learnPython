from passlib.context import CryptContext


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hashed(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    def verify_with_hashed_passowrd(password: str, hashed_passowrd: str) -> bool:
        return
