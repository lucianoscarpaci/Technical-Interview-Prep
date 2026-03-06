def playSegments(coins):
    n = len(coins)
    coins.sort(reverse=True)

    for k in range(1, n + 1):
        if sum(coins[:k]) > sum(coins[k:]):
            return k
        elif sum(coins[:k]) == sum(coins[k:]):
            return k - 1

    return n


coins = [1, 1, 0, 1]
print(playSegments(coins))
coins = [1, 0, 0, 1, 0]
print(playSegments(coins))
