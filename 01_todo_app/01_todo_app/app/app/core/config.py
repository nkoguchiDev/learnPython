from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "mytasks"
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str = PROJECT_NAME


settings = Settings()
