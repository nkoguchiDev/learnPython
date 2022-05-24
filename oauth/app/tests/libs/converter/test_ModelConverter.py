import pytest
from pydantic import BaseModel

from app.libs.converter import ModelConverter

testdata = [[{"name": 'name0'},
             '{name: "name0",description: "-"}'],
            [{"name": 'name0',
              "description": 'description1'},
             '{name: "name0",description: "description1"}']]


class TestModelConverter:
    @pytest.mark.parametrize("data,result", testdata)
    def test_to_cypher_object(self, data, result):
        class Model(BaseModel):
            name: str
            description: str = "-"

        assert ModelConverter.to_cypher_object(Model(**data)) == result
