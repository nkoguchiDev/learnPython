

from app import crud
from app.tests.utils.generator import random_str


email = random_str(7) + '@gmail.com'
password = random_str(7)


class TestCRUDUser:

    def test_create(self, db):
        result = crud.user.create(db=db,
                                  email=email,
                                  password=password)
        assert result['email'] == email

    # def test_get(self, db):
    #     result = crud.user.get(db, id=_user["id"])

    #     assert len(result) == 1
    #     assert result[0]['email'] == email

    # def test_delete(self, db):
    #     crud.user.delete(db, id=_user["id"])
    #     result = crud.user.get(db, id=email)

    #     assert len(result) == 0
