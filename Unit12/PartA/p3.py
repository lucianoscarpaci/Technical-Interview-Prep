def aang_wins(n):
    dp = [False] * (n + 1)
    # Base case if n = 0, Aang loses
    dp[0] = False
    # Fill the dp array
    for i in range(1, n + 1):
        # Aang wins if he can force Zuko into a losing position
        dp[i] = not dp[i - 1] or (i >= 2 and not dp[i - 2])
    # Return if Aang wins on the nth day
    return dp[n]

print(aang_wins(2))
print(aang_wins(3))