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
from kivy.clock import Clock
from menus import *
from leaderboard import Leaderboard
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
        Clock.schedule_interval(lambda dt: print("fps: " + str(Clock.get_fps())), 2)

        self.current_state = GameState.MENU
        self.leaderboard = Leaderboard()
        self.leaderboard.load()

        #move to its own function (sm stuff)
        self.screen_manager = ScreenManager()

        mm = Screen(name='MainMenuScreen')
        self.screen_manager.add_widget(mm)
        mm.add_widget(MainMenuScreen(self.screen_manager, self.transition_state))

        gp = Screen(name='GamePlayScreen')
        self.screen_manager.add_widget(gp)
        self.gameplay_screen = GamePlayScreen(self.screen_manager, self.transition_state)
        gp.add_widget(self.gameplay_screen)

        rules = Screen(name='RulesScreen')
        self.screen_manager.add_widget(rules)
        rules.add_widget(RulesScreen(self.screen_manager, self.transition_state))

        settings = Screen(name='SettingsScreen')
        self.screen_manager.add_widget(settings)
        self.settings_screen = SettingsScreen(self.screen_manager, self.transition_state)
        settings.add_widget(self.settings_screen)

        lb = Screen(name='LeaderboardScreen')
        self.screen_manager.add_widget(lb)
        self.leaderboard_screen = LeaderboardScreen(self.screen_manager, self.transition_state, self.leaderboard)
        lb.add_widget(self.leaderboard_screen) 

        cm = Screen(name='CustomisationScreen')
        self.screen_manager.add_widget(cm)
        self.customisation_screen = CustomisationScreen(self.screen_manager, self.transition_state, self.gameplay_screen, self.leaderboard)
        cm.add_widget(self.customisation_screen) 

        self.screen_manager.current = 'MainMenuScreen'

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
            self.screen_manager.current = 'MainMenuScreen'
            pass
        elif newState == GameState.GAMEPLAY:
            self.screen_manager.current = 'GamePlayScreen'
            self.current_game = Game(self.gameplay_screen, self.leaderboard, self.settings_screen.difficulty)
            self.gameplay_screen.game_over_color = [0, 0, 0, 0]
        elif newState == GameState.SETTINGS:
            self.screen_manager.current = 'SettingsScreen'
        elif newState == GameState.LEADERBOARD:
            self.leaderboard_screen.update_text()
            self.screen_manager.current = 'LeaderboardScreen'
        elif newState == GameState.CUSTOMISATION:
            self.customisation_screen.update_score()
            self.customisation_screen.update_options()
            self.screen_manager.current = 'CustomisationScreen'
        else:
            self.screen_manager.current = 'RulesScreen'

        self.current_state = newState

if __name__ == "__main__":
    Builder.load_file('noteAttack.kv')
    NoteAttack().run()