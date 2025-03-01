class GameState:
    def __init__(self):
        self.__score = 0
        self.__paused = False

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


game_state = GameState()
