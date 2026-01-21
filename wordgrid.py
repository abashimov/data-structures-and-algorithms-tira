class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.y = len(grid)
        self.x = len(grid[0])

    def count(self, word):

        if len(word) == 1:
            return sum(row.count(word) for row in self.grid)

        all_directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (1, -1),
            (-1, 1), (-1, -1),
        ]

        target = min(word, word[::-1])
        if word == word[::-1]:
            directions = [
                (1, 0),
                (0, 1),
                (1, 1),
                (1, -1),
            ]
        else:
            directions = all_directions

        total = 0

        for y in range(self.y):
            for x in range(self.x):
                for dx, dy in directions:
                    if self.match(x, y, dx, dy, target):
                        total += 1

        return total


    def match(self, x, y, dx, dy, target):
        for i in range(len(target)):
            ny = y + dy * i
            nx = x + dx * i
            if ny < 0 or ny >= self.y or nx < 0 or nx >= self.x:
                return False
            if self.grid[ny][nx] != target[i]:
                return False
            
        return True
        
if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0 