import math

def check_number(number):
    num = 0
    given = [3, 7, 1, 3, 7, 1, 3, 7]

    if len(given) != len(number)-1 or number[0] != "0":
        return False
    
    try:
        for i in range(len(given)):
            num += given[i] * int(number[i])
    except ValueError: 
        return False
    
    rounded = math.ceil(num / 10) * 10

    return rounded - num == int(number[-1])

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False