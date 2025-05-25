from __future__ import annotations

from game.elements.bounded_sprite import BoundedSprite

# Base class for game objects


class CircleShape(BoundedSprite):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def collides(self, other: CircleShape):
        return self.position.distance_to(other.position) <= self.radius + other.radius
