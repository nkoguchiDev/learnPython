import pytest


from pydantic import BaseModel

from app import crud


class User(BaseModel):
    name: str
    email: str
    description: str
    price: str
    tax: str


_user = {
    "name": 'name0',
    "email": 'email1',
    "description": 'description1',
    "price": 'price2',
    "tax": 'tax3'
}


class TestCRUDBase:

    def test_create(self, db):
        result = crud.base.create(db, User(**_user))
        set_id(result[0]['id'])
        assert result[0]['name'] == _user['name']

    def test_get(self, db):
        _result = crud.base.create(db, User(**_user))
        result = crud.base.get(db, id=_result["id"])

        assert len(result) == 1
        assert result[0]['email'] == _user['email']
