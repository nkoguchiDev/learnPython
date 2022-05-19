from neo4j import GraphDatabase

from app.core.config import settings
from app.libs.converter import ModelConverter


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
                        {ModelConverter.to_cypher_object(data)})
                RETURN {settings.RECORD_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.RECORD_NODE_NAME)
                for record in result.data()]

    def update(self,
               db: GraphDatabase,
               id: str,
               data: object) -> list:
        query = f"""
                MATCH ({settings.RECORD_NODE_NAME}:{settings.RECORD_NODE_LABEL})
                WHERE {settings.RECORD_NODE_NAME}.id='{id}'
                SET {settings.RECORD_NODE_NAME} = {ModelConverter.to_cypher_object(data)}
                RETURN {settings.RECORD_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.RECORD_NODE_NAME)
                for record in result.data()]

    def delete(self, db: GraphDatabase, id: str) -> None:
        query = f"""
                MATCH({settings.RECORD_NODE_NAME}:{settings.RECORD_NODE_LABEL})
                WHERE {settings.RECORD_NODE_NAME}.id='{id}'
                DELETE {settings.RECORD_NODE_NAME}
                """
        db.run(query)


base = Base()
