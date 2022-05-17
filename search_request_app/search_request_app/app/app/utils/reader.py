from dataclasses import dataclass
from pydantic import BaseModel


path = "./container/nginx/01/log/access.log"
settings_calam_max_num = 9


@dataclass
class CalamNum:
    remote_addr: int = 0
    time_local: int = 1
    request_method: int = 2
    request_uri: int = 3
    status_code: int = 4
    body_bytes_sent: int = 5
    request_time: int = 6
    http_user_agent: int = 7
    http_x_forwarded_for: int = 8
    request_id: int = 9


c_num = CalamNum()


class Reader:
    def __init__(self, path):
        self._path = path

    def read(self):
        with open(self._path) as f:
            self._record = [record for record in f.readlines()]

    def get(self):
        for calam in self._record:
            calam = calam.split(", ")

            record = Record(**{
                "remote_addr": calam[c_num.remote_addr],
                "time_local": calam[c_num.time_local],
                "request_method": calam[c_num.request_method],
                "request_uri": calam[c_num.request_uri],
                "status_code": calam[c_num.status_code],
                "request_id": calam[c_num.request_id],
            })

            print(record.__dict__)


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
    request_id: str = "-"


if __name__ == '__main__':
    reader = Reader(path)
    reader.read()
    reader.get()
