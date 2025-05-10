import sys

import pygame

from constants import (
    PLAYER_MAX_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_TURN_SPEED,
    UI_COLOUR,
)
from game.elements.circleshape import CircleShape
from game.elements.explosion import Explosion
from game.elements.shot import Shot
from game.game_state import Game_State
from groups import drawable, updatable


class Player(CircleShape):
    containers = (updatable, drawable)

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.__initial_pos = pygame.Vector2(x, y)
        self.speed = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, speed):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * speed

    def shoot(self):
        if self.shot_timer > 0:
            return

        pos: pygame.Vector2 = self.position
        shot = Shot(pos.x, pos.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            if self.speed > 0:
                self.speed = 0
            self.speed -= dt * 10
        if keys[pygame.K_w]:
            if self.speed < 0:  #
                self.speed = 0
            self.speed += dt * 10

        # Clamp speed
        self.speed = pygame.math.clamp(self.speed, -PLAYER_MAX_MOVE_SPEED, PLAYER_MAX_MOVE_SPEED)
        self.move(self.speed)

        self.shot_timer -= dt

    def respawn(self, lives: int):
        self.explosion = Explosion(self.position.x, self.position.y, UI_COLOUR)
        if lives == 0:
            print(f"Game over! {Game_State.score} points!")
            # TODO: Do something other than just yeet the world
            sys.exit()
        self.position = pygame.Vector2(self.__initial_pos)
        self.rotation = 0
        self.speed = 0
        self.shot_timer = 0
