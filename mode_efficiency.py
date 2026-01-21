import random, time

def find_mode_dict(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1
        
        if count[x] > count[mode]:
            mode = x
 
    return mode

def find_mode_sorting(numbers):
    nums = sorted(numbers)
    count = 1
    longest = 1
    longest_value = nums[0]
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            count += 1
        else:
            count = 1
        if count > longest:
            longest = count
            longest_value = nums[i]
    return longest_value

if __name__=="__main__":
    numbers = [random.randint(1, 1000) for _ in range(10**7)]
    
    start1 = time.time()
    find_mode_dict(numbers)
    end1 = time.time()
    print("With dict: ", end1 - start1)

    start2 = time.time()
    find_mode_sorting(numbers)
    end2 = time.time()
    print("With sorting: ", end2 - start2)