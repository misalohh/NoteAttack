
LEADERBOARD_SIZE = 5
SAVE_FILE = 'leaderboard.txt'

class Leaderboard:
    leaderboards = [[], [], []] # easy, medium, hard leaderboard
    cumulative_score = 0

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

    def get(self, difficulty):
        return self.leaderboards[int(difficulty)]
    
    def load(self):
        pass

    def save(self):
        pass
    