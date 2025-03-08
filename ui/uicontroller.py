import pygame
from pygame.event import Event

from ui.game import GameUI
from ui.menu import MainMenu
from ui.pause import PauseMenu
from ui.ui import UIBase


class UIController:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.main_menu = MainMenu(self)
        self.pause = PauseMenu(self)
        self.game = GameUI(self)
        self.ui: UIBase = self.main_menu

    def set_ui(self, state):
        if state == "main_menu":
            self.ui = self.main_menu
        elif state == "pause":
            self.ui = self.pause
        elif state == "game":
            self.ui = self.game

        self.draw()

    def draw(self):
        self.ui.draw(self.screen, self.font)

    def update(self):
        pass

    def handle_event(self, event: Event):
        self.ui.handle_event(event)
