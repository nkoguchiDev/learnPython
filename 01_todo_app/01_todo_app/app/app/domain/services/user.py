from app.domain.repositories.user import UserRepository


class UserService:
    def __init__(self) -> None:
        self._user_repo = UserRepository()

    def is_exist(self, email: str) -> bool:
        return self._user_repo.get_by_email(email=email) is not None
