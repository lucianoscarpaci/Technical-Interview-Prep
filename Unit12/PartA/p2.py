def toph_training(cost):
    n = len(cost)

    if n == 1:
        return cost[0]
    
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    # Fill the dp array
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    # Return the minimum cost to reach the last day
    return min(dp[n - 1], dp[n - 2])

print(toph_training([10, 15, 20]))
print(toph_training([1, 100, 1, 1, 200]))
print(toph_training([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
