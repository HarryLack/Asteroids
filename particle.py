import pygame
import math

from groups import drawable

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, speed: float = 0.0, direction: float = 0.0):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.position = pygame.Vector2(x, y)

        #TODO: Understand and Fix this calc,
        vel_x = speed*math.sin(direction)
        vel_y = speed*math.cos(direction)
        self.velocity = pygame.Vector2(vel_x, vel_y)
        print(self.velocity)


    def update(self, dt):
        self.position += self.velocity * dt


    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.position)
