from app.infrastructure.database.connection import db


class UserDatabase:
    def __init__(self) -> None:
        self._db = db
