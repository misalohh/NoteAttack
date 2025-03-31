from kivy.uix.floatlayout import FloatLayout
from enum import Enum

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class BaseMenu(FloatLayout):
    def __init__(self, screen_manager, transition_state, **kwargs):
        super(BaseMenu, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.transition_state = transition_state

class MainMenu(BaseMenu):
    pass

class GamePlay(BaseMenu):
    pass

class Rules(BaseMenu):
    pass

class Settings(BaseMenu):
    def __init__(self, screen_manager, transition_state, **kwargs):
        super().__init__(screen_manager, transition_state, **kwargs)
        self.difficulty = Difficulty.MEDIUM
    def set_difficulty(self, difficulty):
        print('changing difficulty: ' + str(self.difficulty) + ' -> ' + str(Difficulty(difficulty)))
        self.difficulty = Difficulty(difficulty)


class Leaderboard(BaseMenu):
    pass