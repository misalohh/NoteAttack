
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from difficulty import Difficulty

DIFFICULTY_TO_SPEED = {
    Difficulty.EASY: 5,
    Difficulty.MEDIUM: 3,
    Difficulty.HARD: 1
}

LASER_TIMEOUT_MS = 500

class Character(Widget):
    pass

class Game:
    def __init__(self, gameplay_screen, leaderboard, difficulty):
        self.leaderboard = leaderboard
        self.difficulty = difficulty
        self.enemies_list = []
        self.score = 0
        self.is_game_over = False
        self.start_enemies()
        self.gameplay_screen = gameplay_screen
        self.gameplay_screen.reset_score()
        self.speed = DIFFICULTY_TO_SPEED[difficulty]
        self.last_laser_time = 0
        print("starting new " + str(difficulty) + " game!")

    def handle_gameplay_input(self, key):
        # todo: use ord for all keys
        if key == ord('a'):
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
        # for testing
        # elif key == ord('1'):
        #     self.score += 10
        #     self.gameplay_screen.update_score(self.score)


    def start_enemies(self):
        print("Starting enemy appearance")
        self.enemy_event = Clock.schedule_interval(self.enemy_appears, 3)

    def enemy_appears(self, dt):
        from Sprites.enemies import Enemies

        if self.is_game_over:
            return

        print("adding enemy")
        enemy = Enemies(self)
        self.gameplay_screen.add_widget(enemy)
        self.enemies_list.append(enemy)
        enemy.move_to_centre(self.speed)

    def stop_enemies(self):
        print("Stopping enemy appearance")
        if self.enemy_event:
            self.enemy_event.cancel()
            self.enemy_event = None
    
    def create_laser(self, note):
        from Sprites.laser import Laser

        # don't spawn laser before timeout
        t = Clock.get_time()
        delta_ms = (t - self.last_laser_time) * 1000.
        if delta_ms < LASER_TIMEOUT_MS:
            print("timeout")
            return

        self.last_laser_time = t

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
            self.increase_score()
            self.gameplay_screen.remove_widget(enemy)
            self.enemies_list.remove(enemy) 

    def increase_score(self):
        self.score += 1
        self.gameplay_screen.update_score(self.score)
    
    def end_game(self):
        self.stop_enemies()

        # remove remaining enemies
        for enemy in self.enemies_list:
            print("removing enemy, game over")
            self.gameplay_screen.remove_widget(enemy)
            self.enemies_list.remove(enemy) 

        if self.is_game_over:
            return
        
        self.is_game_over = True
        print('Game over')
        self.leaderboard.add_score(self.score, self.difficulty)
        print('score: ' + str(self.score))
        print(str(self.difficulty) + ' leaderboard: ' + str(self.leaderboard.get(self.difficulty)))
        print(self.score)
