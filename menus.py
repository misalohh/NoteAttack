from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from difficulty import Difficulty

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
    easy_color = ListProperty([151/255, 104/255, 196/255, 1])
    medium_color = ListProperty([151/255, 104/255, 196/255, 1]) 
    hard_color = ListProperty([151/255, 104/255, 196/255, 1])  
    def __init__(self, screen_manager, transition_state, **kwargs):
        super().__init__(screen_manager, transition_state,  **kwargs)
        self.difficulty = Difficulty.MEDIUM
        
    def set_difficulty(self, difficulty):
        print('changing difficulty: ' + str(self.difficulty) + ' -> ' + str(Difficulty(difficulty)))
        self.difficulty = Difficulty(difficulty)

        if self.difficulty == Difficulty.EASY:
            self.easy_color = [136/255, 83/255, 172/255, 1]
        else:
            self.easy_color = [151/255, 104/255, 196/255, 1]

        if self.difficulty == Difficulty.MEDIUM:
            self.medium_color = [136/255, 83/255, 172/255, 1]
        else:
            self.medium_color = [151/255, 104/255, 196/255, 1]

        if self.difficulty == Difficulty.HARD:
            self.hard_color = [136/255, 83/255, 172/255, 1]
        else:
            self.hard_color = [151/255, 104/255, 196/255, 1]

class Customisation(BaseMenu):
    pass

class Leaderboard(BaseMenu):
    pass  