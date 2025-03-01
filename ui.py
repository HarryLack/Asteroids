import pygame

class UI:
    def __init__(self, screen:pygame.Surface):
        self.screen = screen

    def draw(self):
        print("ui draw")

    def update(self):
        print("ui update")
