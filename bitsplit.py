def count_splits(sequence):
    zeros = sequence.count("0")
    ones = sequence.count("1")
    if zeros != ones:
        return 0
    zeros = 0
    ones = 0
    result = 0
    for i in range(len(sequence)-1):
        if sequence[i] == "0":
            zeros += 1
        if sequence[i] == "1":
            ones += 1
        if ones == zeros:
            result += 1
    return result


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999