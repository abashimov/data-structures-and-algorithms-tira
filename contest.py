class Contest:
    def __init__(self, names, task_count):
        self.task_count = task_count
        self.time = 0
        self.scores = {}
        self.reach_time = {}
        for _ in names:
            self.scores[_] = [0] * self.task_count
            self.reach_time[_] = 0

    def add_submission(self, name, task, score):
        self.time += 1
        if self.scores[name][task-1] < score:
            self.scores[name][task-1] = score
            self.reach_time[name] = self.time 

    def create_scoreboard(self):
        contestants = []
        for name in self.scores:
            total_score = sum(self.scores[name])
            reach_time = self.reach_time[name]
            contestants.append((name, total_score, reach_time))
        contestants.sort(key=lambda c:(-c[1], c[2]) if c[1] > 0 else (0, 0, c[0]))
        result = []
        for c in contestants:
            result.append((c[0], c[1]))
        return result

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]