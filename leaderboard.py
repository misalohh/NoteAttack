import csv
import os

LEADERBOARD_SIZE = 5
SAVE_FILE = 'leaderboard.csv'
NEW_LEADER_BOARD = [[0 for _ in range(5)] for _ in range(3)]

class Leaderboard:
    leaderboards = [[], [], []] 
    cumulative_score = 0

    def new_save_file(self):
        print('Creating new save file.')
        self.leaderboards = NEW_LEADER_BOARD
        self.save()

    def load(self):
        print('loading save file')

        if not os.path.isfile(SAVE_FILE):
            print('Save file did not exist.')
            self.new_save_file()
            return

        with open(SAVE_FILE, mode = 'r', newline = '') as csvfile:
            reader = csv.reader(csvfile)
            if not any(reader):  
                print('The file is empty.')
                self.new_save_file()
                return
            for row in reader:
                # load cumulative score
                if row[1] == 'X':
                    self.cumulative_score = int(row[0])
                    print('loading cumulative score: ' + row[0])
                    continue

                score = int(row[0])  
                difficulty = int(row[1]) 
                self.leaderboards[difficulty].append(score) 
                print('loading: ' + row[0], row[1])

    def save(self):
        print('saving leaderboard')
        with open(SAVE_FILE, mode = 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['score', 'difficulty'])
            for difficulty in range(3):
                leaderboard = self.leaderboards[difficulty]
                for score in leaderboard:
                    writer.writerow([score, difficulty])
                writer.writerow([self.cumulative_score, 'X'])

    def add_score(self, score, difficulty):
        self.cumulative_score += score
        inserted = False
        leaderboard = self.leaderboards[int(difficulty)]
        for i in range(0, min(LEADERBOARD_SIZE, len(leaderboard))):
            if score > leaderboard[i]:
                leaderboard.insert(i, score)
                inserted = True
                break

        if not inserted and len(leaderboard) < LEADERBOARD_SIZE:
            leaderboard.append(score)

        if inserted and len(leaderboard) > LEADERBOARD_SIZE:
            leaderboard.pop()
        
        print(self.leaderboards)
        self.save()

    def get(self, difficulty):
        return self.leaderboards[int(difficulty)]
