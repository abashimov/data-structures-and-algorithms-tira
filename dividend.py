def find_profits(prices):
    result = []
    min_price = prices[0]
    for i in range(len(prices)):
        if prices[i] + i < min_price:
            min_price = prices[i] + i
        price = (prices[i] + i) - min_price
        result.append(price)
    return result

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 2, 4, 6]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 1, 2, 3]
    print(find_profits([2, 4, 1, 3])) # [0, 3, 1, 4]
    print(find_profits([1, 1, 5, 1])) # [0, 1, 6, 3]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 2, 5, 2, 6]

    # prices = list(range(1, 10**5+1))
    # print(find_profits(prices)[:5]) # [0, 2, 4, 6, 8]