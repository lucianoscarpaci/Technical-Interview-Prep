def max_profit(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        if price < min_price:
            min_price = min(price, min_price)
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

prices_1 = [7,1,5,3,6,4]
prices_2 = [7,6,4,3,1]
print(max_profit(prices_1))  # Output: 5
print(max_profit(prices_2))  # Output: 0
prices_3 = [9, 1, 4, 3, 2, 4]
print(max_profit(prices_3))