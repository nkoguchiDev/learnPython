from pymongo import MongoClient

from app.core.config import settings

client = MongoClient(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
)
db = client[settings.DB_NAME]
