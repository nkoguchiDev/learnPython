import uuid


from app import crud


data = {
    "id": uuid.uuid4().hex,
    "key": uuid.uuid4().hex,
    "secret": uuid.uuid4().hex,
}


class TestCRUDClientCredential:

    def test_create(self, cache):
        result = crud.token.create(cache, data)
        assert result['key'] == data['key']
        assert result['secret'] == data['secret']

    def test_get(self, cache):
        result = crud.token.get(cache, id=data["id"])

        assert len(result) == 0

    def test_delete(self, cache):
        crud.token.delete(cache, id=data["id"])
        result = crud.token.get(cache, id=data["id"])

        assert len(result) == 0
