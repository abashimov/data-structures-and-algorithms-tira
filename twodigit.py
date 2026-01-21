def count_numbers(a, b):
    numbers = [2, 5]
    count = 0

    while numbers:
        x = numbers.pop(0)
        if x > b:
            continue
        if x >= a:
            count += 1
        numbers.append(x * 10 + 2)
        numbers.append(x * 10 + 5)

    return count

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512