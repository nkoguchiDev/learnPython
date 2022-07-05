from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_DB_USER: str
    MONGO_DB_PASSWORD: str
    MONGO_DB_HOST: str
    MONGO_DB_PORT: int


settings = Settings()
