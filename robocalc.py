def calculate(input, rules):
    complete_input = list("L" + input + "R")
    pos = 0
    state = 1
    counter = 0
    result = False

    while counter < 1000:
        current = complete_input[pos]
        found = False
        for rule in rules:
            if rule[0] == current and rule[1] == state:
                found = True
                complete_input[pos] = rule[2]
                state = rule[3]
                if rule[4] == "LEFT":
                    pos -= 1
                elif rule[4] == "RIGHT":
                    pos += 1
                elif rule[4] == "ACCEPT":
                    return True
                elif rule[4] == "REJECT":
                    return False

                if pos < 0 or pos >= len(complete_input):
                    return False

                break
        if not found:
            return False

        counter += 1
    return result


if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False