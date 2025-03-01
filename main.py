import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UI_COLOUR
from player import Player
from asteroidfield import AsteroidField
from groups import updatable, drawable, asteroids, shots
import time


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    pygame.font.init()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 16)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    start_time = time.time()
    dt = 0
    score = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    _ = AsteroidField()

    paused = False
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused


        if paused:
            continue
        else:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.collides(player):
                    print(f"Game over! {score} points!")
                    sys.exit()

                for s in shots:
                    if s.collides(a):
                        score += a.split()
                        s.kill()

            screen.fill(pygame.Color(0, 0, 0))

            for d in drawable:
                d.draw(screen)

            text = font.render(f"{score}", True, "#ffffff")
            screen.blit(text, [0,0])

            time_elapsed = time.gmtime(time.time()-start_time)
            time_text = font.render(f"{time.strftime('%M:%S', time_elapsed)}", True, UI_COLOUR)
            screen.blit(time_text, [200,0])

            pygame.display.flip()
            dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
