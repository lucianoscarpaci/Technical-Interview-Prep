def zuko_supply_mission(tokens, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 tokens needed to reach amount 0

    for token in tokens:
        for i in range(token, amount + 1):
            dp[i] = min(dp[i], dp[i - token] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(zuko_supply_mission([1, 2, 5], 11))
print(zuko_supply_mission([2], 3))
print(zuko_supply_mission([1], 0))
