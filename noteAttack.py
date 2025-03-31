import kivy
kivy.require('2.3.0')
from kivy.config import Config
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '960')

from enum import Enum
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from menus import Leaderboard, Rules, Settings, GamePlay, MainMenu, Customisation
from game import Game

class GameState(Enum):
    MENU = 0
    GAMEPLAY = 1
    RULES = 2
    SETTINGS = 3
    LEADERBOARD = 4
    CUSTOMISATION = 5

class NoteAttack(App):
    def build(self):
        Window.bind(on_key_down=self.handle_input)

        self.current_state = GameState.MENU
        self.screen_manager = ScreenManager()

        mm = Screen(name='MainMenu')
        self.screen_manager.add_widget(mm)
        mm.add_widget(MainMenu(self.screen_manager, self.transition_state))

        gp = Screen(name='GamePlay')
        self.screen_manager.add_widget(gp)
        self.gameplay_screen = GamePlay(self.screen_manager, self.transition_state)
        gp.add_widget(self.gameplay_screen)

        rules = Screen(name='Rules')
        self.screen_manager.add_widget(rules)
        rules.add_widget(Rules(self.screen_manager, self.transition_state))

        settings = Screen(name='Settings')
        self.screen_manager.add_widget(settings)
        self.settings_screen = Settings(self.screen_manager, self.transition_state)
        settings.add_widget(self.settings_screen)

        lb = Screen(name='Leaderboard')
        self.screen_manager.add_widget(lb)
        lb.add_widget(Leaderboard(self.screen_manager, self.transition_state)) 

        cm = Screen(name='Customisation')
        self.screen_manager.add_widget(cm)
        cm.add_widget(Customisation(self.screen_manager, self.transition_state)) 
 

        self.screen_manager.current = 'MainMenu'

        return self.screen_manager

    def handle_input(self, window, key, *args):
        if self.current_state == GameState.GAMEPLAY:
            self.current_game.handle_gameplay_input(key)

    def transition_state(self, newState):
        newState = GameState(newState)
        print("transitioning game state " + str(self.current_state) + " -> " + str(newState))
        if self.current_state == GameState.MENU:
            self.screen_manager.transition = SlideTransition(direction='left')
        elif newState == GameState.CUSTOMISATION:
            self.screen_manager.transition = SlideTransition(direction='left')
        else:
            self.screen_manager.transition = SlideTransition(direction='right')
        
        if self.current_state == GameState.GAMEPLAY:
            self.current_game.end_game()

        if newState == GameState.MENU:
            self.screen_manager.current = 'MainMenu'
            pass
        elif newState == GameState.GAMEPLAY:
            self.screen_manager.current = 'GamePlay'
            self.current_game = Game(self.gameplay_screen, self.settings_screen.difficulty)
        elif newState == GameState.SETTINGS:
            self.screen_manager.current = 'Settings'
        elif newState == GameState.LEADERBOARD:
            self.screen_manager.current = 'Leaderboard'
        elif newState == GameState.CUSTOMISATION:
            self.screen_manager.current = 'Customisation'
        else:
            self.screen_manager.current = 'Rules'

        self.current_state = newState

if __name__ == "__main__":
    Builder.load_file('noteAttack.kv')
    NoteAttack().run()