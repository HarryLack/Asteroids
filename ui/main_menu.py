from typing import TYPE_CHECKING

import pygame

from game.game_state import GAME_MODE, Game_State
from ui.ui import UI_MODE, UIBase

if TYPE_CHECKING:
    from ui.uicontroller import UIController


class MainMenu(UIBase):
    def __init__(self, parent: "UIController"):
        super().__init__(parent)
        self.options = ["Start Game", "Options", "Exit"]
        self.selected_option = 0

    def update(self):
        pass

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        for i, opt in enumerate(self.options):
            text = font.render(opt, True, (255, 255, 255))
            if i == self.selected_option:
                text = font.render(opt, True, (0, 255, 0))
            screen.blit(
                text,
                (
                    screen.get_width() // 2 - text.get_width() // 2,
                    screen.get_height() // 2 - text.get_height() // 2 + i * 50,
                ),
            )

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    self.parent.set_ui(UI_MODE.GAME)
                    Game_State.state = GAME_MODE.PLAY
                elif self.selected_option == 1:
                    pass
                elif self.selected_option == 2:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
