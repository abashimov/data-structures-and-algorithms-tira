def create_distribution(string):
    seen = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            seen.add(string[i:j])

    results = {}
    for i in seen:
        if len(i) not in results:
            results[len(i)] = 0
        results[len(i)] += 1

    return dict(sorted(results.items()))

if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}