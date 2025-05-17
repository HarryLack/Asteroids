from __future__ import annotations

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    containers = None
    position: pygame.Vector2 = pygame.Vector2(1_000_000)

    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if self.containers:
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def edge_check(self):
        if self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT

    def collides(self, other: CircleShape):
        return self.position.distance_to(other.position) <= self.radius + other.radius
