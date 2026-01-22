import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    ls = []
    for i in range(comparer.list_size()):
        left = 0
        right = len(ls)
        while left < right:
            mid = (left + right) // 2
            if comparer.smaller(i, ls[mid]):
                right = mid
            else:
                left = mid + 1
        ls.insert(left, i)
    result = [0] * len(ls)
    value = 1
    for pos in ls:
        result[pos] = value
        value += 1
    return result

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]