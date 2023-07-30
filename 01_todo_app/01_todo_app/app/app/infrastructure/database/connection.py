from pymongo import MongoClient

from app.core.config import settings

client = MongoClient(settings.DB_CONNECTION_STRING)
db = client[settings.PROJECT_NAME]
