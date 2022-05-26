from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    password: str
    is_active = True
    is_super = False


class ClientCredential(BaseModel):
    id: str
    key: str
    secret: str


class Token(BaseModel):
    developerId: str
    # refresh_token: str = None
    # expires_in: int = None
    # scope: str = None
    # client_id: str = None
