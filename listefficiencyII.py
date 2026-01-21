import time

def insertion(n):
    ls = []
    for i in range(1, n+1):
        ls.append(i)
    return ls

def delete_from_beginning(ls):
    while ls:
        ls.pop(0)

if __name__=="__main__":
    start = time.time()
    result = insertion(10**5)
    end = time.time()
    print(f"insertion time: {end - start} s")

    start = time.time()
    result = delete_from_beginning(result)
    end = time.time()
    print(f"deletion time: {end - start} s")