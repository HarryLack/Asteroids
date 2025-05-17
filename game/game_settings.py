class GameSettings:
    def __init__(self):
        self.__invincible = False

    @property
    def invincible(self):
        return self.__invincible

    @invincible.setter
    def score(self, value: bool):
        self.__invincible = value


Game_Settings = GameSettings()
