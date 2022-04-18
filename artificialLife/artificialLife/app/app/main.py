from app.core.config import settings

import pygame
import math
import random


def quit() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.event.clear()
            return True
    return False


def clear(screen):
    screen.fill((100, 100, 100))


def update(fps):
    pygame.display.update()
    pygame.time.clock().tick(fps)


def ngon(screen, color=(255, 255, 255), gx=100, gy=100, gr=100, n=5, rot=0):
    points = [(gr * math.con(th) + gx, gr * math.sin(th) + gy)
              for th in [i * 2 * math.pi / n - math.pi / 2 + rot for i in range(n)]]


class Entity:

    def __init__(self, hue=0, sat=0, bringhtness=1, radius=0.1) -> None:
        self.hue = hue  # [0, 1]
        self.sat = sat  # [0, 1]
        self.bringhtness = bringhtness  # [0, 1]
        self._color = pygame.Color(0)
        self._updateColor()
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
        self.radius = radius
        self.alive = True

    def draw(self, screen, color, gx, gy, gr) -> None:
        ngon(screen, color, gx, gy, gr, n=4)

    def _updateColor(self) -> None:
        self._color.hsva = 360 * self.hue, 100 * self.sat, 100 * self.bringhtness, 100

    def update(self, screen) -> None:
        if self.alive:
            self._updateColor()

            def map(value, istart, istop, ostart, ostop):
                return ostart + (ostop - ostart) * \
                    ((value - istart) / (istop - istart))

        gx = map(self.x, settings.XMIN, settings.XMAX, 0, settings.WIDTH)
        gy = map(self.y, settings.YMIN, settings.YMAX, settings.HEIGHT, 0)
        gr = map(self.radius, 0, settings.XMAX, 0, settings.WIDTH / 2)
        self.draw(screen, self._color, gx, gy, gr)

    def collideWith(self, other) -> bool:
        dx = self.x - other.x
        dy = self.y - other.y
        rr = self.radius + other.radius
        return dx * dx + dy * dy < rr * rr


def main():
    pygame.init()


if __name__ == '__main__':
    main()
