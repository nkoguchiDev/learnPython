import random
from dataclasses import dataclass


@dataclass
class Node:
    life: int = 0
    alive: bool = True
    x: int = 0
    y: int = 0


class common:
    def __init__(self, node: Node):
        if node.life == 0:
            self.life = random.randrange(1, 10)
        else:
            self.life = node.life

        self.alive = node.alive
        self.x = node.x
        self.y = node.y

    def move(self):
        self.x += random.randrange(-10, 10)
        self.y += random.randrange(-10, 10)
        self.life -= 1
        if self.life <= 0:
            self.alive = False
