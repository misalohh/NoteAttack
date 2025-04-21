from kivy.core.window import Window
from kivy.uix.widget import Widget
from game import Game
from kivy.animation import Animation
from kivy.properties import StringProperty
from difficulty import Difficulty
import random

NOTES_MAP = {
    Difficulty.EASY: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    Difficulty.MEDIUM: ['A', 'A#', 'B','B#', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#'],
    Difficulty.HARD: ['A', 'A#', 'B','B#', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb']
}
class Enemies(Widget):
    note = StringProperty('A')

    def get_difficulty(self):
        return self.game_instance.get_current_difficulty()
    
    def __init__(self, game_instance, **kwargs):
        super(Enemies, self).__init__(**kwargs)
        self.game_instance = game_instance
        self.difficulty = self.get_difficulty()
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.note = random.choice(NOTES_MAP[self.difficulty])
        self.set_random_offscreen()

    def set_random_offscreen(self):
        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            self.pos = (-self.width, random.uniform(0, Window.height))
        elif side == 'right':
            self.pos = (Window.width, random.uniform(0, Window.height))
        elif side == 'top':
            self.pos = (random.uniform(0, Window.width), Window.height)
        elif side == 'bottom':
            self.pos = (random.uniform(0, Window.width), -self.height)

    def move_to_centre(self, speed):
        centre_x = (Window.width / 2) - (self.width / 2)
        centre_y = (Window.height / 2) - (self.height / 2)
        animation = Animation(x = centre_x, y = centre_y, duration = speed)
        animation.bind(on_complete=self.on_reach)
        animation.start(self)

    def on_reach(self, *args):
        if self.parent:
            self.parent.remove_widget(self)
            self.game_instance.enemies_list.remove(self)
            self.game_instance.end_game()
        else:
            print("Enemy already removed, skipping.")
