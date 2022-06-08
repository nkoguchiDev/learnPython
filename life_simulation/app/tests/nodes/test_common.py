from app.nodes.common import common
from dataclasses import dataclass


@dataclass
class Node:
    life: int = 0
    alive: bool = True
    x: int = 0
    y: int = 0


class TestCommon:
    def test_move_and_stop(self):
        node = common(Node())
        life = node.life

        for i in range(life - 1):
            node.move()
            print(node.life, node.x, node.y)
        assert node.alive is True

        node.move()
        assert node.alive is False
