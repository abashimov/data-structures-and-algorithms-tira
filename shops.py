def find_distances(street):
    go_right = []
    some_number = 10**7
    found1 = False
    count = 0
    for i in range(len(street)):
        if street[i] == "1":
            go_right.append(0)
            count = 0
            found1 = True
        elif found1:
            go_right.append(count)
        elif not found1:
            go_right.append(some_number)
        count += 1

    go_left = []
    found1 = False
    count = 0
    for i in range(len(street)-1, -1, -1):
        if street[i] == "1":
            go_left.append(0)
            count = 0
            found1 = True
        elif found1:
            go_left.append(count)
        elif not found1:
            go_left.append(some_number)
        count += 1

    go_left = list(reversed(go_left))

    result = []
    for i in range(len(street)):
        result.append(min(go_right[i], go_left[i]))
    return result
        

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663