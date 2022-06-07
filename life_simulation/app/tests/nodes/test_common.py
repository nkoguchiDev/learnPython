from app.nodes.common import common


class TestCommon:
    def test_move_and_stop(self):
        node = common()

        for i in range(10):
            node.move()
        assert node.alive is False
