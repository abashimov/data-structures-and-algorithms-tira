def count_splits(numbers):
    count_right = {}
    for i in numbers:
        if i not in count_right:
            count_right[i] = 0
        count_right[i] += 1
    count_left = {}
    total_unique = len(count_right)
    right_unique = total_unique
    left_unique = 0
    result = 0
    for i in range(len(numbers)-1):
        if numbers[i] not in count_left:
            count_left[numbers[i]] = 0
            left_unique += 1
        count_left[numbers[i]] += 1
        count_right[numbers[i]] -= 1
        if count_right[numbers[i]] <= 0:
            right_unique -= 1
        if left_unique == total_unique and right_unique == total_unique:
            result += 1
    return result

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1