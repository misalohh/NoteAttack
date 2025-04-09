
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from difficulty import Difficulty

LEADERBOARD_SIZE = 5

class Character(Widget):
    pass

class Game:
    def __init__(self, gameplay_screen, difficulty):
        self.difficulty = difficulty
        self.enemies_list = []
        self.score = 0
        self.start_enemies()
        self.gameplay_screen = gameplay_screen
        self.leaderboards = [[], [], []] # easy, medium, hard leaderboard
        print("starting new " + str(difficulty) + " game!")

    def handle_gameplay_input(self, key):
        if key == 97:
            self.create_laser('A')
        elif key == 98:
            self.create_laser('B')
        elif key == 99:
            self.create_laser('C')
        elif key == 100:
            self.create_laser('D')
        elif key == 101:
            self.create_laser('E')
        elif key == 102:
            self.create_laser('F')
        elif key == 103:
            self.create_laser('G')

    def start_enemies(self):
        print("Starting enemy appearance")
        if self.difficulty == Difficulty.HARD:
            speed = 1
        if self.difficulty == Difficulty.MEDIUM:
            speed = 3
        if self.difficulty == Difficulty.EASY:
            speed = 6 # the duration not the interval
        else:
            speed = 3
        self.enemy_event = Clock.schedule_interval(self.enemy_appears, speed)

    def enemy_appears(self, dt):
        from Sprites.enemies import Enemies
        enemy = Enemies(game_instance=self)
        self.gameplay_screen.add_widget(enemy)
        self.enemies_list.append(enemy)
        enemy.move_to_centre()

    def stop_enemies(self):
        print("Stopping enemy appearance")
        if self.enemy_event:
            self.enemy_event.cancel()
            self.enemy_event = None
    
    def create_laser(self, note):
        from Sprites.laser import Laser
        laser = Laser(self, note)
        self.gameplay_screen.add_widget(laser)  
        print("Laser added successfully: {laser}")  
        Clock.schedule_once(lambda dt: laser.grow(), 0) 

    def check_laser_collision(self, laser):
        laser_x, laser_y = Window.width / 2, Window.height / 2
        to_remove = []

        for enemy in self.enemies_list:
            if enemy.note != laser.note:
                continue

            enemy_x, enemy_y = enemy.pos
            enemy_center = (enemy_x + enemy.width / 2, enemy_y + enemy.height / 2)
            distance = ((laser_x - enemy_center[0])**2 + (laser_y - enemy_center[1])**2) ** 0.5

            if distance <= laser.radius: 
                to_remove.append(enemy)

        for enemy in to_remove:
            self.score += 1
            self.gameplay_screen.remove_widget(enemy)
            self.enemies_list.remove(enemy) 

    def end_game(self):
        print(self.score)
        self.stop_enemies()
        inserted = False
        for i in range(0, min(LEADERBOARD_SIZE, len(self.leaderboards))):
            if self.score > self.leaderboards[i]:
                self.leaderboards[self.difficulty].insert(i, self.score)
                inserted = True

        if not inserted and len(self.leaderboards) < LEADERBOARD_SIZE:
            self.leaderboards[self.difficulty].append(self.score)

        if inserted and len(self.leaderboards) > LEADERBOARD_SIZE:
            self.leaderboards[self.difficulty].pop()

        print(self.leaderboards)