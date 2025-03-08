import sys
import time

import pygame

from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from gamestate import game_state
from groups import asteroids, drawable, shots, updatable
from player import Player
from ui.uicontroller import UIController


def main():
    print("Starting asteroids!")

    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("./assets/background.png")

    ui_controller = UIController(screen, font)
    clock = pygame.time.Clock()
    game_state.start_time = time.time()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not game_state.paused:
                        ui_controller.set_ui("pause")
                    else:
                        ui_controller.set_ui("game")

                    game_state.paused = not game_state.paused

            ui_controller.handle_event(event)

    ui_controller.set_ui("game")
    # Game Loop
    while True:
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(background, (0, 0))
        handle_events()

        if not game_state.paused:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.collides(player):
                    game_state.player_lives -= 1
                    if game_state.player_lives == 0:
                        print(f"Game over! {game_state.score} points!")
                        sys.exit()
                    else:
                        player.respawn()

                for s in shots:
                    if s.collides(a):
                        game_state.score += a.split()
                        s.kill()

            dt = clock.tick(60) / 1000

        for d in drawable:
            d.draw(screen)

        ui_controller.update()
        ui_controller.draw()
        pygame.display.flip()

    print("Goodbye")


if __name__ == "__main__":
    main()
