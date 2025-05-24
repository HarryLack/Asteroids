import pygame

from game.elements.weapons.shot import Shot
from game.elements.weapons.weapon import Weapon
from game.elements.weapons.weapon_config import BASE_DAMAGE, BASE_RANGE, BASE_RATE, BASE_SPEED


class Gun(Weapon):
    def __init__(self):
        super().__init__(BASE_SPEED, BASE_DAMAGE, BASE_RANGE, BASE_RATE)

    def shoot(self, position: pygame.Vector2, angle: int):
        if self.timer > 0:
            return

        shot = Shot(position.x, position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(angle) * self.speed

        self.timer = self.rate
        pass
