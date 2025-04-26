import random

import pygame

from constants import ASTEROID_BASE_SCORE, ASTEROID_MIN_RADIUS
from game.elements.circleshape import CircleShape
from groups import asteroids, drawable, updatable


class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self):
        self.kill()

    def split(self):
        self.explode()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ASTEROID_BASE_SCORE // self.radius

        angle = random.uniform(20, 50)
        pos_angle = self.velocity.rotate(angle)
        neg_angle = self.velocity.rotate(-angle)

        pos: pygame.Vector2 = self.position
        first = Asteroid(pos.x, pos.y, self.radius - ASTEROID_MIN_RADIUS)
        first.velocity = pos_angle * 1.2
        second = Asteroid(pos.x, pos.y, self.radius - ASTEROID_MIN_RADIUS)
        second.velocity = neg_angle * 1.2

        return ASTEROID_BASE_SCORE // self.radius
