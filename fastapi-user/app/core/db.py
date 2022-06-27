import motor.motor_asyncio
from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from app.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    username=settings.MONGO_DB_USER,
    password=settings.MONGO_DB_PASSWORD,
    host=settings.MONGO_DB_HOST,
    port=settings.MONGO_DB_PORT,
    uuidRepresentation="standard"
)
db = client["database_name"]


class User(BeanieBaseUser[PydanticObjectId]):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
