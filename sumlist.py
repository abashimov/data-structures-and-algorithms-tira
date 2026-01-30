class SumList:
    def __init__(self):
        self.sums = []
        self.current = 0

    def append(self, number):
        self.sums.append(self.current + number)
        self.current += number

    def sum(self, a, b):
        return self.sums[b] - self.sums[a-1] if a-1 >= 0 else self.sums[b]

if __name__ == "__main__":
    numbers = SumList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        total += numbers.sum(i // 2, i)
    print(total) # 125005000050000