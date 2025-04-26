from game.elements.particle import Particle
from groups import drawable, updatable

MIN_PARTICLES = 5
MAX_PARTICLES = 10


class Explosion:
    def __init__(self, x: float, y: float, color) -> None:
        self.particles = []
        self.timer = 0
        count = 1  # random.randint(MIN_PARTICLES, MAX_PARTICLES)
        for i in range(count):
            dir = 360 / count * i
            print("dir", dir)
            particle = Particle(x, y, color, 5, speed=10.0, direction=dir)
            particle.add(drawable, updatable)
            self.particles.append(particle)

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
