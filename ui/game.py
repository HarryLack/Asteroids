import time
from typing import TYPE_CHECKING

from constants import UI_COLOUR
from game.game_state import Game_State
from ui.ui import UIBase

if TYPE_CHECKING:
    from ui.uicontroller import UIController


class GameUI(UIBase):
    def __init__(self, parent: "UIController"):
        super().__init__(parent)

    def update(self):
        pass

    def draw(self, screen, font):
        text = font.render(f"{Game_State.score}", True, UI_COLOUR)
        screen.blit(text, [0, 0])
        time_elapsed = time.gmtime(time.time() - Game_State.start_time)
        time_text = font.render(f"{time.strftime('%M:%S', time_elapsed)}", True, UI_COLOUR)
        screen.blit(time_text, [200, 0])
        lives_text = font.render(f"Lives: {Game_State.player_lives}", True, UI_COLOUR)
        screen.blit(lives_text, [400, 0])
