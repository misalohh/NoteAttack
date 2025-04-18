from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty
from difficulty import Difficulty

# todo: load all of this from files
UNSELECTED_COLOUR = [151/255, 104/255, 196/255, 1]
SELECTED_COLOUR = [136/255, 83/255, 172/255, 1]

DEFAULT_BACKGROUND = [189/255, 158/255, 219/255, 1]
DEFAULT_SKIN = [115/255, 61/255, 153/255, 1]
DEFAULT_BUTTON = [115/255, 61/255, 153/255, 1]
DEFAULT_LINE =  [63/255, 22/255, 92/255, 1]

BACKGROUND_COLOUR_MAP = {
    'Default': DEFAULT_BACKGROUND,
    'Pink': [184/255, 70/255, 167/255,1],
    'Blue': [63/255, 119/255, 209/255, 1], 
    'Red': [214/255, 71/255, 75/255, 1], 
    'Orange': [230/255, 136/255, 90/255, 1], 
    'Green': [103/255, 140/255, 88/255, 1], 
    'Outer Space': [40/255, 19/255, 66/255, 1]
}
SKIN_COLOUR_MAP = {
    'Default': DEFAULT_SKIN,
    'Pink': [171/255, 24/255, 102/255,1],
    'Blue': [17/255, 51/255, 173/255, 1], 
    'Red': [171/255, 24/255, 34/255, 1], 
    'Orange': [196/255, 77/255, 26/255, 1], 
    'Green': [31/255, 99/255, 25/255, 1], 
    'Mars': [168/255, 66/255, 22/255, 1] 
}
BUTTON_COLOUR_MAP = {
    'Default': DEFAULT_BUTTON,
    'Pink': [171/255, 24/255, 102/255,1],
    'Blue': [17/255, 51/255, 173/255, 1], 
    'Red': [171/255, 24/255, 34/255, 1], 
    'Orange': [196/255, 77/255, 26/255, 1], 
    'Green': [31/255, 99/255, 25/255, 1], 
    'Outer Space': [168/255, 66/255, 22/255, 1] 
}
CHARACTER_LINE_COLOUR_MAP = {
    'Default': DEFAULT_LINE,
    'Pink': [94/255, 8/255, 45/255,1],
    'Blue': [5/255, 11/255, 77/255, 1], 
    'Red': [97/255, 5/255, 5/255, 1], 
    'Orange': [97/255, 33/255, 5/255, 1], 
    'Green': [9/255, 48/255, 12/255, 1], 
    'Mars': [115/255, 35/255, 13/255, 1] 
}
LINE_COLOUR_MAP = {
    'Default': DEFAULT_LINE,
    'Pink': [94/255, 8/255, 45/255,1],
    'Blue': [5/255, 11/255, 77/255, 1], 
    'Red': [97/255, 5/255, 5/255, 1], 
    'Orange': [97/255, 33/255, 5/255, 1], 
    'Green': [9/255, 48/255, 12/255, 1], 
    'Outer Space': [115/255, 35/255, 13/255, 1] 
}

THEME_UNLOCK_MAP = {
    'Pink': 0,
    'Blue': 10, 
    'Red': 20, 
    'Orange': 30, 
    'Green': 40, 
    'Outer Space': 50
}

SKIN_UNLOCK_MAP = {
    'Pink': 0,
    'Blue': 10, 
    'Red': 20, 
    'Orange': 30, 
    'Green': 40, 
    'Mars': 50
}

class BaseMenu(FloatLayout):
    def __init__(self, screen_manager, transition_state, **kwargs):
        super(BaseMenu, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.transition_state = transition_state

# todo: change all names to add screen (not in quotes only in class)
class MainMenu(BaseMenu):
    pass

class Customisation(BaseMenu):
    score_text = StringProperty('Points: 0')
    theme_options = ListProperty(['monkey'])
    skin_options = ListProperty(['monkey'])

    def __init__(self, screen_manager, transition_state, gameplay_screen, leaderboard, **kwargs):
        super().__init__(screen_manager, transition_state, **kwargs)
        self.gameplay_screen = gameplay_screen
        self.leaderboard = leaderboard

    def update_options(self):
        self.theme_options.append('madness')
        self.theme_options = [theme for theme, required_score in THEME_UNLOCK_MAP.items() if self.leaderboard.cumulative_score >= required_score]
        self.skin_options = [skin for skin, required_score in SKIN_UNLOCK_MAP.items() if self.leaderboard.cumulative_score >= required_score]

    def on_theme_spinner(self, text):
        self.gameplay_screen.background_colour = BACKGROUND_COLOUR_MAP[text]
        self.gameplay_screen.button_colour = BUTTON_COLOUR_MAP[text]
        self.gameplay_screen.line_colour = LINE_COLOUR_MAP[text]  

    def on_skin_spinner(self, text):
        self.gameplay_screen.skin_colour = SKIN_COLOUR_MAP[text] 
        self.gameplay_screen.character_line_colour = CHARACTER_LINE_COLOUR_MAP[text]

    def update_score(self):
        self.score_text = "Points: " + str(self.leaderboard.cumulative_score)

class GamePlay(BaseMenu):
    background_colour = ListProperty(DEFAULT_BACKGROUND)
    skin_colour = ListProperty(DEFAULT_SKIN)
    button_colour = ListProperty(DEFAULT_BUTTON)
    line_colour = ListProperty(DEFAULT_LINE)
    character_line_colour = ListProperty(DEFAULT_LINE)
    score = StringProperty('0')

    def update_score(self, score):
        self.score = str(score)
    
    def reset_score(self):
        self.score = '0'

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
    # todo: make a list?
    easy_text = StringProperty("test")
    medium_text = StringProperty("test")
    hard_text = StringProperty("test")

    def __init__(self, screen_manager, transition_state, leaderboard, **kwargs):
        self.leaderboard = leaderboard
        super().__init__(screen_manager, transition_state,  **kwargs)

    def update_text(self):
        self.easy_text = self.get_leaderboard_text(Difficulty.EASY)
        self.medium_text = self.get_leaderboard_text(Difficulty.MEDIUM)
        self.hard_text = self.get_leaderboard_text(Difficulty.HARD)

    def get_leaderboard_text(self, difficulty):
        leaderboard = self.leaderboard.get(difficulty)
        text = ""
        for i in range(len(leaderboard)):
            text += str(i + 1) + ": " + str(leaderboard[i])
            if not i == (len(leaderboard) - 1):
                text += "\n"
        return text