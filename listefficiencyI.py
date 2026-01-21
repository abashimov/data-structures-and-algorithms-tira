import time

def insert_elements(n):
    ls = []
    for i in range(1, n+1):
        ls.append(i)
    return ls

def deletion(ls):
    while ls:
        ls.pop()

if __name__=="__main__":
    start = time.time()
    result = insert_elements(10**5)
    end = time.time()
    print("for insertion: ", end - start, "s")

    start = time.time()
    result = deletion(result)
    end = time.time()
    print("for deletion: ", end - start, "s")