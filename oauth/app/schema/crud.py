from pydantic import BaseModel


class User(BaseModel):
    id: str = None
    email: str = None
    password: str = None


class ClientCredential(BaseModel):
    id: str = None
    key: str = None
    secret: str = None


class Token(BaseModel):
    id: str = None
    access_token: str = None
    # refresh_token: str = None
    # expires_in: int = None
    # scope: str = None
    # client_id: str = None
