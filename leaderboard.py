
LEADERBOARD_SIZE = 5
SAVE_FILE = 'leaderboard.txt'

class Leaderboard:
    leaderboards = [[], [], []] # easy, medium, hard leaderboard

    def add_score(self, score, difficulty):
        inserted = False
        leaderboard = self.leaderboards[int(difficulty)]
        for i in range(0, min(LEADERBOARD_SIZE, len(leaderboard))):
            if self.score > leaderboard[i]:
                leaderboard.insert(i, score)
                inserted = True

        if not inserted and len(leaderboard) < LEADERBOARD_SIZE:
            leaderboard.append(score)

        if inserted and len(leaderboard) > LEADERBOARD_SIZE:
            leaderboard.pop()

        print(self.leaderboards)

    def get(self, difficulty):
        return self.leaderboards[int(difficulty)]
    
    def load(self):
        pass

    def save(self):
        pass
    