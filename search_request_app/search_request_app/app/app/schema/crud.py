from pydantic import BaseModel


class Request(BaseModel):
    id: str = None
    remote_addr: str = None
    time_local: str = None
    request_method: str = None
    request_uri: str = None
    status_code: int = None
    body_bytes_sent: int = None
    request_time: float = None
    http_user_agent: str = None
    http_x_forwarded_for: str = None
    request_id: str = None
