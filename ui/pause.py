import pygame
from pygame.event import Event

from gamestate import game_state
from ui.ui import UIBase

menu_options = ["Resume", "Options", "Quit"]


class PauseMenu(UIBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected_option = 0

    def update(self):
        pass

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        for i, opt in enumerate(menu_options):
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
        pass

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    game_state.paused = False
                elif self.selected_option == 1:
                    pass
                elif self.selected_option == 2:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
