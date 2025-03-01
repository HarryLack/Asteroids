import pygame
from pygame.event import Event

from ui.menu import Menu
from ui.pause import PauseMenu
from ui.ui import UIBase


class UIController:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.main_menu = Menu(self)
        self.pause = PauseMenu(self)
        self.ui: UIBase = self.main_menu

    def set_ui(self, state):
        if state == "main_menu":
            self.ui = self.main_menu
        elif state == "pause":
            self.ui = self.pause

        self.draw()

    def draw(self):
        self.ui.draw(self.screen, self.font)

    def update(self):
        pass

    def handle_event(self, event: Event):
        self.ui.handle_event(event)
