import uuid


from app import crud


data = {
    "id": uuid.uuid4().hex,
    "remote_addr": "172.18.0.1",
    "time_local": "[23/May/2022:16:35:26 +0000]",
    "request_method": 'GET',
    "request_uri": '/',
    "status_code": 200,
    "body_bytes_sent": 615,
    "request_time": 0.000,
    "httpdata_agent": 'PostmanRuntime/7.29.0',
    "http_x_forwarded_for": '-',
    "request_id": uuid.uuid4().hex,
}


class TestCRUDBase:

    def test_create(self, db):
        result = crud.request.create(db, data)
        assert result[0]['request_id'] == data['request_id']

    def test_get(self, db):
        result = crud.request.get(db, id=data["id"])

        assert len(result) == 1
        assert result[0]['remote_addr'] == data['remote_addr']

    def test_update(self, db):
        update_request_id = uuid.uuid4().hex
        result = crud.request.update(
            db, id=data["id"], data={
                "request_id": update_request_id})

        assert len(result) == 1
        assert result[0]['request_id'] == update_request_id

    def test_delete(self, db):
        crud.request.delete(db, id=data["id"])
        result = crud.request.get(db, id=data["id"])

        assert len(result) == 0
