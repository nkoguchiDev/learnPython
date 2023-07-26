class UserRepository:
    def __init__(self, database) -> None:
        self._db = database.users
