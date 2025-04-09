from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from difficulty import Difficulty

UNSELECTED_COLOUR = [151/255, 104/255, 196/255, 1]
SELECTED_COLOUR = [136/255, 83/255, 172/255, 1]

class BaseMenu(FloatLayout):
    def __init__(self, screen_manager, transition_state, **kwargs):
        super(BaseMenu, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.transition_state = transition_state


class MainMenu(BaseMenu):
    pass

class GamePlay(BaseMenu):
    score = '0'

class Rules(BaseMenu):
    pass

class Settings(BaseMenu):
    easy_color = ListProperty(UNSELECTED_COLOUR)
    medium_color = ListProperty(SELECTED_COLOUR)
    hard_color = ListProperty(UNSELECTED_COLOUR)

    def __init__(self, screen_manager, transition_state, **kwargs):
        super().__init__(screen_manager, transition_state,  **kwargs)
        self.difficulty = Difficulty.MEDIUM
        
    def set_difficulty(self, difficulty):
        print('changing difficulty: ' + str(self.difficulty) + ' -> ' + str(Difficulty(difficulty)))
        self.difficulty = Difficulty(difficulty)

        if self.difficulty == Difficulty.EASY:
            self.easy_color = SELECTED_COLOUR
        else:
            self.easy_color = UNSELECTED_COLOUR
            print('easy unuselect')

        if self.difficulty == Difficulty.MEDIUM:
            self.medium_color = SELECTED_COLOUR
        else:
            self.medium_color = UNSELECTED_COLOUR
            print('medium unuselect')


        if self.difficulty == Difficulty.HARD:
            self.hard_color = SELECTED_COLOUR
        else:
            self.hard_color = UNSELECTED_COLOUR
            print('hard unuselect')


class Customisation(BaseMenu):
    pass

class Leaderboard(BaseMenu):
    pass  