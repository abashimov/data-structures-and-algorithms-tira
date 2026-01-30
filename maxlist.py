class MaxList:
    def __init__(self):
        self.maxx = None

    def append(self, number):
        if self.maxx == None:
            self.maxx = number
        self.maxx = max(self.maxx, number)

    def max(self):
        return self.maxx

if __name__ == "__main__":
    numbers = MaxList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total) # 99498381797517