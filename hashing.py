def hash_value(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = i
    n = len(string)-1
    value = 0
    for i in string:
        value += dictionary[i] * (23**n)
        n -= 1
    value = value % 2**32
    return value

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440