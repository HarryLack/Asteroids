from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from ui.uicontroller import UIController


class UIBase:
    def __init__(self, parent: "UIController"):
        self.parent = parent

    def update(self):
        # sub-classes must override
        pass

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        # sub-classes must override
        pass

    def handle_event(self, event: pygame.event.Event):
        # sub-classes must override
        pass
