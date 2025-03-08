import time
from typing import TYPE_CHECKING

from constants import UI_COLOUR
from gamestate import game_state
from ui.ui import UIBase

if TYPE_CHECKING:
    from ui.uicontroller import UIController


class GameUI(UIBase):
    def __init__(self, parent: "UIController"):
        super().__init__(parent)

    def update(self):
        pass

    def draw(self, screen, font):
        text = font.render(f"{game_state.score}", True, UI_COLOUR)
        screen.blit(text, [0, 0])
        if game_state.start_time is not None:
            time_elapsed = time.gmtime(time.time() - game_state.start_time)
            time_text = font.render(f"{time.strftime('%M:%S', time_elapsed)}", True, UI_COLOUR)
            screen.blit(time_text, [200, 0])
