class RepeatList:
    def __init__(self):
        self.dict = {}
        self.result = False

    def append(self, number):
        if number not in self.dict:
            self.dict[number] = 0
        self.dict[number] += 1
        if self.dict[number] > 1:
            self.result = True

    def repeat(self):
        return self.result

if __name__ == "__main__":
    numbers = RepeatList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 12345)
        if numbers.repeat():
            total += 1
    print(total) # 87655