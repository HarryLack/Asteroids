from enum import Enum

from constants import PLAYER_STARTING_LIVES

GAME_MODE = Enum("State", ["MENU", "PLAY", "PAUSE"])


class GameState:
    def __init__(self):
        self.__score = 0
        self.__start_time = 0.0
        self.__player_lives = PLAYER_STARTING_LIVES
        self.__state: GAME_MODE = GAME_MODE.MENU

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value: GAME_MODE):
        self.__state = value

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @property
    def player_lives(self):
        return self.__player_lives

    @player_lives.setter
    def player_lives(self, value):
        self.__player_lives = value


Game_State = GameState()
