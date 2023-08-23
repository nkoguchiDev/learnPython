from app.core.config import settings
from mongoengine import connect

db = connect(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    uuidRepresentation="standard",
    alias=settings.PROJECT_NAME,
)
