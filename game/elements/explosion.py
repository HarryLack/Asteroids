import random

import pygame

from game.elements.particle import Particle
from groups import drawable, updatable

MIN_PARTICLES = 5
MAX_PARTICLES = 10
EXPLOSION_TIME = 0.5
EXPLOSION_SPEED = 250.0


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, color) -> None:
        super().__init__()
        self.add(updatable)
        self.particles: list[Particle] = []
        self.timer = 0
        count = random.randint(MIN_PARTICLES, MAX_PARTICLES)
        for i in range(count):
            dir = 360 / count * i
            particle = Particle(x, y, color, 5, speed=EXPLOSION_SPEED, direction=dir)
            particle.add(drawable, updatable)
            self.particles.append(particle)

    def update(self, dt):
        self.timer += dt
        print(self.timer)
        if self.timer >= EXPLOSION_TIME:
            for particle in self.particles:
                particle.kill()
            self.kill()
