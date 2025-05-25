import pygame

from game.elements.weapons.shot import Shot
from game.elements.weapons.weapon import Weapon
from game.elements.weapons.weapon_config import SHOTGUN_CONFIG

# Total spread angle
MAX_SPREAD = 90


class Shotgun(Weapon):
    def __init__(self):
        super().__init__(
            SHOTGUN_CONFIG["speed"], SHOTGUN_CONFIG["damage"], SHOTGUN_CONFIG["range"], SHOTGUN_CONFIG["rate"]
        )
        self.__bullets = SHOTGUN_CONFIG["bullets"]

    def shoot(self, position: pygame.Vector2, angle: int):
        if self.timer > 0:
            return

        start = angle - (MAX_SPREAD // 2)
        spread = MAX_SPREAD / (self.__bullets - 1)
        for i in range(self.__bullets):
            dir = start + (spread * i)
            shot = Shot(position.x, position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(dir) * self.speed

        self.timer = self.rate
        pass
