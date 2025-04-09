from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty
from difficulty import Difficulty

UNSELECTED_COLOUR = [151/255, 104/255, 196/255, 1]
SELECTED_COLOUR = [136/255, 83/255, 172/255, 1]
DEFAULT_BACKGROUND = [189/255, 158/255, 219/255, 1]
BACKGROUND_COLOUR_MAP = {
    'Default': DEFAULT_BACKGROUND,
    'Pink': [1,0,0,1]
}


class BaseMenu(FloatLayout):
    def __init__(self, screen_manager, transition_state, **kwargs):
        super(BaseMenu, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.transition_state = transition_state

# change all names to add screen (not in quotes only in class)
class MainMenu(BaseMenu):
    pass

class Customisation(BaseMenu):
    def __init__(self, screen_manager, transition_state, gameplay_screen, **kwargs):
        super().__init__(screen_manager, transition_state,  **kwargs)
        self.gameplay_screen = gameplay_screen

    def on_spinner(self, spinner, text):
        self.gameplay_screen.background_colour = BACKGROUND_COLOUR_MAP[text]
        

class GamePlay(BaseMenu):
    background_colour = ListProperty(DEFAULT_BACKGROUND)
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

        if self.difficulty == Difficulty.MEDIUM:
            self.medium_color = SELECTED_COLOUR
        else:
            self.medium_color = UNSELECTED_COLOUR


        if self.difficulty == Difficulty.HARD:
            self.hard_color = SELECTED_COLOUR
        else:
            self.hard_color = UNSELECTED_COLOUR


class LeaderboardScreen(BaseMenu):
    def __init__(self, screen_manager, transition_state, leaderboard, **kwargs):
        self.leaderboard = leaderboard
        self.easy_text = StringProperty()
        super().__init__(screen_manager, transition_state,  **kwargs)

    def get_leaderboard_text(self, difficulty):
        leaderboard = self.leaderboard.get(difficulty)
        print('getting lb text ' + str(leaderboard))
        print('difficulty ' + str(difficulty))
        print(self.leaderboard.leaderboards)
        return str(leaderboard)
        #check length
        #return "1:" + leaderboard[0] + "\n2:\n3:\n4:\n5:"