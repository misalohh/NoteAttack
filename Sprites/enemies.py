from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import StringProperty
import random

Notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

class Enemies(Widget):
    note = StringProperty('A')
    def __init__(self, **kwargs):
        super(Enemies, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.note = random.choice(Notes)
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

    def move_to_centre(self):
        centre_x =(Window.width / 2 - self.width / 2)
        centre_y = (Window.height / 2 - self.height / 2)
        animation = Animation(x=centre_x, y= centre_y, duration= 3)
        animation.bind(on_complete=self.on_reach)
        animation.start(self)

    def on_reach(self, *args):
        from game import Game
        if self.parent:
            print('Game Over')
            self.parent.remove_widget(self)
            self.stop_enemies()
        else:
            print(f"⚠️ Enemy {self} already removed, skipping.")
