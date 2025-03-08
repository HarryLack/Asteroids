from constants import PLAYER_STARTING_LIVES


class GameState:
    def __init__(self):
        self.__score = 0
        self.__paused = False
        self.__start_time = 0.0
        self.__player_lives = PLAYER_STARTING_LIVES

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def paused(self):
        return self.__paused

    @paused.setter
    def paused(self, value):
        self.__paused = value

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


game_state = GameState()
