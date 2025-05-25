import pygame


class Weapon:
    def __init__(self, speed, damage, range, rate: float):
        self.speed: int = speed
        self.damage = damage
        self.range = range
        self.rate: float = rate
        self.timer = 0

    def shoot(self, position: pygame.Vector2, angle: int):
        # TBI per subclass
        pass

    def update(self, dt):
        self.timer -= dt
