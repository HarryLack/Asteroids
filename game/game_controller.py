import sys
import time

import pygame

from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, UI_COLOUR
from explosion import Explosion
from gamestate import game_state
from groups import asteroids, drawable, shots, updatable
from player import Player
from ui.uicontroller import UIController


class GameController:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load("./assets/background.png")
        self.ui_controller = UIController(self.screen)
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self._ = AsteroidField()

        self.test_particle = Explosion(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, UI_COLOUR)

    def run(self):
        game_state.start_time = time.time()
        while True:
            self.handle_events()
            self.update(self.dt)
            self.draw()

        print("Goodbye")

    def handle_events(self):
        for event in pygame.event.get():
            # Core Events
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not game_state.paused:
                        self.ui_controller.set_ui("pause")
                    else:
                        self.ui_controller.set_ui("game")

                    game_state.paused = not game_state.paused

                # Temp
                if event.key == pygame.K_RETURN:
                    test_particle = Explosion(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, UI_COLOUR)

            # UI Events
            self.ui_controller.handle_event(event)

    def update(self, dt):
        if not game_state.paused:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.collides(self.player):
                    game_state.player_lives -= 1
                    if game_state.player_lives == 0:
                        print(f"Game over! {game_state.score} points!")
                        sys.exit()
                    else:
                        self.player.respawn()

                for s in shots:
                    if s.collides(a):
                        game_state.score += a.split()
                        s.kill()

            self.dt = self.clock.tick(60) / 1000

        self.ui_controller.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for d in drawable:
            d.draw(self.screen)
        self.ui_controller.draw()
        pygame.display.flip()
