from passlib.context import CryptContext


def to_hashed_passowrd(password: str) -> str:
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)
