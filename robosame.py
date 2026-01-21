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

def create_rules():
    rules = []
    
    return rules

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False