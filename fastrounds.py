def count_rounds(numbers):
    size = len(numbers)
    count_dips = 1
    pos = {}
    for i in range(len(numbers)):
        pos[numbers[i]] = i

    for i in range(2, size + 1):
        if pos[i] < pos[i-1]:
            count_dips += 1
            
    return count_dips

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000