import time
import random

# implementation 1
def count_even_first(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even_second(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__=="__main__":
    random.seed(1337)
    data = [random.randint(1, 10**6) for _ in range(10000)]
    start_time1 = time.time()
    result1 = count_even_first(data)
    end_time1 = time.time()
    start_time2 = time.time()
    result2 = count_even_second(data)
    end_time2 = time.time()

    print("Result of first algo: ", result1)
    print("Time: ", round(end_time1 - start_time1, 4), "s")
    print("Result of second algo: ", result2)
    print("Time: ", round(end_time2 - start_time2, 4), "s")