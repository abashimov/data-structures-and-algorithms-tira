def count_pairs(numbers):
    if len(numbers) < 2:
        return 0
    ls = sorted(numbers)
    A = 0
    B = len(ls) // 2
    count = 0
    while A < len(ls) // 2 and B < len(ls):
        if 2 * ls[A] <= ls[B]:
            count += 1
            A += 1
            B += 1
        else:
            B += 1
    return count 

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176