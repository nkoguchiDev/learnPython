from uuid import uuid4
import string
import secrets
import random


class ValueGenerator:
    @staticmethod
    def random_chara(num: int) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(num))

    def random_email(domain: str = "domain.dummy.com") -> str:
        return f"{ValueGenerator.random_chara(random.randint(10, 20))}@{domain}"

    def random_uuid() -> str:
        return str(uuid4())
