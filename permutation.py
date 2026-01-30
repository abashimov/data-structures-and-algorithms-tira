class PermutationTracker:
    def __init__(self):
        self.set = set()
        self.max = None
        self.duplicate = False

    def append(self, number):
        if number in self.set:
            self.duplicate = True
        self.set.add(number)
        if self.max == None:
            self.max = number
        self.max = max(self.max, number)

    def check(self):
        return True if len(self.set) == self.max and not self.duplicate else False

if __name__ == "__main__":
    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000