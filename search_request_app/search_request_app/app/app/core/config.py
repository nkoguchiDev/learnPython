from pydantic import BaseSettings


class Settings(BaseSettings):
    GRAPH_DB_USER: str = "neo4j"
    GRAPH_DB_PASSWORD: str = "neo4jj"
    GRAPH_DB_HOST: str = "localhost"
    GRAPH_DB_PORT: int = 7687
    RECORD_NODE_NAME: str = "record"
    RECORD_NODE_LABEL: str = "Record"


settings = Settings()
