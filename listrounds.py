def find_rounds(numbers):
    ls = []
    size = len(numbers)
    needed = 1
    while needed <= size:
        current_list = []
        for i in numbers:
            if i == needed:
                current_list.append(i)
                needed += 1
        ls.append(current_list)
    return ls

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]