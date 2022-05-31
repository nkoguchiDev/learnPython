from pydantic import BaseSettings


class Settings(BaseSettings):
    # project settings
    PROJECT_NAME: str = "IAM"
    API_V1_STR: str = "/api/v1"

    # neo4j server settings
    GRAPH_DB_USER: str = "neo4j"
    GRAPH_DB_PASSWORD: str = "neo4jj"
    GRAPH_DB_HOST: str = "localhost"
    GRAPH_DB_PORT: int = 7687

    # cypher query settings
    USER_NODE_NAME: str = "user"
    USER_NODE_LABEL: str = "User"
    TOKEN_NODE_NAME: str = "token"
    TOKEN_NODE_LABEL: str = "Token"

    # redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB_NUM: int = 0


settings = Settings()
