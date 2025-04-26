import pygame

from constants import SHOT_RADIUS
from game.elements.circleshape import CircleShape
from groups import drawable, shots, updatable


class Shot(CircleShape):
    containers = (shots, drawable, updatable)

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
