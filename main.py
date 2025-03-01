import sys
import time

import pygame

from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, UI_COLOUR
from gamestate import game_state
from groups import asteroids, drawable, shots, updatable
from player import Player
from ui.uicontroller import UIController


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ui_controller = UIController(screen, font)
    clock = pygame.time.Clock()
    start_time = time.time()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    # Game Loop
    while True:
        screen.fill(pygame.Color(0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not game_state.paused:
                        ui_controller.set_ui("pause")

                    game_state.paused = not game_state.paused

            ui_controller.handle_event(event)

        if game_state.paused:
            pass
        else:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.collides(player):
                    print(f"Game over! {game_state.score} points!")
                    sys.exit()

                for s in shots:
                    if s.collides(a):
                        game_state.score += a.split()
                        s.kill()

            dt = clock.tick(60) / 1000

        for d in drawable:
            d.draw(screen)

        text = font.render(f"{game_state.score}", True, UI_COLOUR)
        screen.blit(text, [0, 0])

        time_elapsed = time.gmtime(time.time() - start_time)
        time_text = font.render(f"{time.strftime('%M:%S', time_elapsed)}", True, UI_COLOUR)
        screen.blit(time_text, [200, 0])

        ui_controller.update()
        ui_controller.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
