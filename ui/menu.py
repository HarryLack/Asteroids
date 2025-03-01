from typing import TYPE_CHECKING

from ui.ui import UIBase

if TYPE_CHECKING:
    from ui.uicontroller import UIController


class Menu(UIBase):
    def __init__(self, parent: "UIController"):
        super().__init__(parent)
        self.options = ["Start Game", "Options", "Exit"]

    def update(self):
        pass

    def draw(self, screen, font):
        pass
