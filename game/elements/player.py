import sys

import pygame

from constants import (
    PLAYER_MAX_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    UI_COLOUR,
)
from game.elements.circleshape import CircleShape
from game.elements.explosion import Explosion
from game.elements.weapons.gun import Gun
from game.elements.weapons.shotgun import Shotgun
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
        self.__weapons = [Gun(), Shotgun()]
        self.__selected_weapon = 0

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
        self.edge_check()

    def shoot(self):
        self.__weapons[self.__selected_weapon].shoot(self.position, self.rotation)

    def __slow(self, dt):
        if self.speed > 0:
            self.speed -= dt * 15
        elif self.speed < 0:
            self.speed += dt * 15

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()
        # Move
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            if self.speed > 0:
                self.speed = 0
            self.speed -= dt * 10
        elif keys[pygame.K_w]:
            if self.speed < 0:
                self.speed = 0
            self.speed += dt * 10
        else:
            self.__slow(dt)

        # Clamp speed
        self.speed = pygame.math.clamp(self.speed, -PLAYER_MAX_MOVE_SPEED, PLAYER_MAX_MOVE_SPEED)
        self.move(self.speed)

        for weapon in self.__weapons:
            weapon.update(dt)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("q")
                self.__selected_weapon = (self.__selected_weapon - 1) % len(self.__weapons)
            elif event.key == pygame.K_e:
                print("e")
                self.__selected_weapon = (self.__selected_weapon + 1) % len(self.__weapons)

    def respawn(self, lives: int):
        self.explosion = Explosion(self.position.x, self.position.y, UI_COLOUR)
        if lives == 0:
            print(f"Game over! {Game_State.score} points!")
            # TODO: Do something other than just yeet the world
            sys.exit()
        self.position = pygame.Vector2(self.__initial_pos)
        self.rotation = 0
        self.speed = 0
        for weapon in self.__weapons:
            weapon.timer = 0
