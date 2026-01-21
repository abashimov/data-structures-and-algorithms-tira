def find_number(numbers):
    for i in range(len(numbers)-2):
        if numbers[i] == numbers[i+1] == numbers[i+2]:
            pass
        elif numbers[i] == numbers[i+1]:
            return numbers[i+2]
        elif numbers[i] == numbers[i+2]:
            return numbers[i+1]
        else:
            return numbers[i]

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100
    print(find_number([1, 1, 1, 1, 1, 1, 7]))

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2