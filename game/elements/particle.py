import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, speed: float = 0.0, direction: float = 0.0):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(speed).rotate(direction)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.position)
