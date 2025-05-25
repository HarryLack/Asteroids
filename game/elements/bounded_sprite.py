from __future__ import annotations

import pygame

from constants import DEFAULT_SCREEN_HEIGHT, DEFAULT_SCREEN_WIDTH


# Base class for game objects
class BoundedSprite(pygame.sprite.Sprite):
    containers = None
    position: pygame.Vector2 = pygame.Vector2(1_000_000)

    def __init__(self, x: float, y: float):
        # we will be using this later
        if self.containers:
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def edge_check(self):
        if self.position.x > DEFAULT_SCREEN_WIDTH:
            self.position.x -= DEFAULT_SCREEN_WIDTH
        if self.position.x < 0:
            self.position.x += DEFAULT_SCREEN_WIDTH
        if self.position.y > DEFAULT_SCREEN_HEIGHT:
            self.position.y -= DEFAULT_SCREEN_HEIGHT
        if self.position.y < 0:
            self.position.y += DEFAULT_SCREEN_HEIGHT
