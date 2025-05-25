import sys
import time

import pygame

from constants import DEFAULT_SCREEN_HEIGHT, DEFAULT_SCREEN_WIDTH
from game.elements.asteroidfield import AsteroidField
from game.elements.player import Player
from game.game_settings import Game_Settings
from game.game_state import GAME_MODE, Game_State
from groups import asteroids, drawable, shots, updatable
from ui.uicontroller import UI_MODE, UIController


class GameController:
    def __init__(self):
        self.screen = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT))
        self.background = pygame.image.load("./assets/background.png")
        self.ui_controller = UIController(self.screen)
        self.ui_controller.set_ui(UI_MODE.MAIN_MENU)
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.player = Player(DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2)
        _ = AsteroidField()

    def run(self):
        Game_State.start_time = time.time()
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
                    if Game_State.state == GAME_MODE.PLAY:
                        self.ui_controller.set_ui(UI_MODE.PAUSE)
                        Game_State.state = GAME_MODE.PAUSE
                    elif Game_State.state == GAME_MODE.PAUSE:
                        self.ui_controller.set_ui(UI_MODE.GAME)
                        Game_State.state = GAME_MODE.PLAY

            # UI Events
            self.ui_controller.handle_event(event)

            self.player.handle_event(event)

    def update(self, dt):
        if Game_State.state == GAME_MODE.PLAY:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if not Game_Settings.invincible and a.collides(self.player):
                    Game_State.player_lives -= 1
                    self.player.respawn(Game_State.player_lives)

                for s in shots:
                    if s.collides(a):
                        Game_State.score += a.split()
                        s.kill()

            self.dt = self.clock.tick(60) / 1000

        self.ui_controller.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if Game_State.state == GAME_MODE.PLAY or Game_State.state == GAME_MODE.PAUSE:
            for d in drawable:
                d.draw(self.screen)
        self.ui_controller.draw()
        pygame.display.flip()
