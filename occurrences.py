class OccurrenceTracker:
    def __init__(self):
        self.nums = {}

    def append(self, number):
        if number not in self.nums:
            self.nums[number] = 0
        self.nums[number] += 1

    def count(self):
        s = set()
        for key, value in self.nums.items():
            s.add(value)
        return len(s)

if __name__ == "__main__":
    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901