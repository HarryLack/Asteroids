import pygame
from pygame.event import Event

from ui.game import GameUI
from ui.main_menu import MainMenu
from ui.pause_menu import PauseMenu
from ui.ui import UI_MODE, UIBase


class UIController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.main_menu = MainMenu(self)
        self.pause = PauseMenu(self)
        self.game = GameUI(self)
        self.ui: UIBase = self.main_menu

    def set_ui(self, ui: UI_MODE):
        if ui == UI_MODE.MAIN_MENU:
            self.ui = self.main_menu
        elif ui == UI_MODE.PAUSE:
            self.ui = self.pause
        elif ui == UI_MODE.GAME:
            self.ui = self.game

        self.draw()

    def draw(self):
        self.ui.draw(self.screen, self.font)

    def update(self):
        pass

    def handle_event(self, event: Event):
        self.ui.handle_event(event)
