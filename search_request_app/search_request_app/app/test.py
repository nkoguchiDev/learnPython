from random import random
from app.db.session import SessionLocal
from app.crud.base import Base

from pydantic import BaseModel


class Record(BaseModel):
    remote_addr: str = "-"
    time_local: str = "-"
    request_method: str = "-"
    request_uri: str = "-"
    status_code: int = "-"
    body_bytes_sent: int = "-"
    request_time: float = "-"
    http_user_agent: str = "-"
    http_x_forwarded_for: str = "-"
    id: str = "-"


if __name__ == '__main__':
    base = Base()
    id_ = "8792jd2hd89h4j38"
    print(base.create(SessionLocal, Record(**{"id": id_})))
    print(base.get(SessionLocal, id_))
