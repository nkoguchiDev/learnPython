from neo4j import GraphDatabase

from app.core.config import settings
from app.utils.converter import modelConverter


class Base:

    def __init__(self):
        pass

    def get(self, db: GraphDatabase, id: str) -> list:
        query = f"""
                MATCH ({settings.RECORD_NODE_NAME}:{settings.RECORD_NODE_LABEL} {{id: '{id}'}})
                RETURN {settings.RECORD_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.RECORD_NODE_NAME)
                for record in result.data()]

    def create(self, db: GraphDatabase, data: object) -> list:
        query = f"""
                CREATE ({settings.RECORD_NODE_NAME}:{settings.RECORD_NODE_LABEL}
                        {modelConverter.to_cypher_object(data)})
                RETURN {settings.RECORD_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.RECORD_NODE_NAME)
                for record in result.data()]


base = Base()
