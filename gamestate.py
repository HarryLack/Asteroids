class GameState:
    def __init__(self):
        self.__score = 0
        self.__paused = False
        self.__start_time = 0.0

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


game_state = GameState()
