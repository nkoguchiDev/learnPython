from pydantic import BaseSettings


class Settings(BaseSettings):
    WIDTH: int = 500
    HEIGHT: int = 500
    FPS: int = 30
    XMIN: int = -1.5
    XMAX: int = 1.5
    YMIN: int = -1.5
    YMAX: int = 1.5


settings = Settings()
