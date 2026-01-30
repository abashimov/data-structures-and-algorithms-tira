class ChangeList:
    def __init__(self):
        self.numbers = []
        self.operations = 0

    def append(self, number):
        self.numbers.append(number - self.operations)

    def get(self, index):
        return self.numbers[index] + self.operations

    def change_all(self, amount):
        self.operations += amount

if __name__ == "__main__":
    numbers = ChangeList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        numbers.change_all(i % 11 - 5)
        total += numbers.get(i // 2)
    print(total) # 2500049970