from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.clock import Clock

class Laser(Widget):
    def __init__(self, game, note, **kwargs):
        super(Laser, self).__init__(**kwargs)
        self.radius = 0
        self.game = game
        self.note = note
        with self.canvas:
            Color(0, 0, 0, 1)  
            self.circle = Line(circle=(Window.width / 2, Window.height / 2, 0), width=2)

    def grow(self):
        animation = Animation(radius=950, duration=1)  
        animation.bind(on_progress=self.update_circle)
        animation.bind(on_complete=self.schedule_destroy)  
        animation.start(self)

    def update_circle(self, *args):
        self.game.check_laser_collision(self)
        self.circle.circle = (Window.width / 2, Window.height / 2, self.radius)

    def schedule_destroy(self, *args):
        Clock.schedule_once(self.destroy, 0.1)  

    def destroy(self, *args):
        if self.parent:
            self.parent.remove_widget(self)
        else:
            print("Laser parent is None, skipping removal to prevent crashs")