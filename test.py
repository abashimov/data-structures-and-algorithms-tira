def max_customers(arrivals, departures):
    time_action = []
    for i in arrivals:
        time_action.append((i, "arrival"))
    for i in departures:
        time_action.append((i, "departure"))

    time_action.sort()

    count = 0
    result = 0

    for i in time_action:
        if i[1] == "arrival":
            count += 1
        elif i[1] == "departure":
            count -= 1
        result = max(result, count)
    
    return count