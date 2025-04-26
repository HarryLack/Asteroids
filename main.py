import pygame

from game.game_controller import GameController


def main():
    print("Starting Asteroids!")

    pygame.init()
    pygame.font.init()

    controller = GameController()
    controller.run()

    print("Goodbye")


if __name__ == "__main__":
    main()
