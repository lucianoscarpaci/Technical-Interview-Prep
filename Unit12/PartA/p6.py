def training_synchronization(katara, toph):
    m, n = len(katara), len(toph)
    # Create a DP table (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Fill the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if katara[i-1] == toph[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(training_synchronization("waterbend", "earthbend"))
print(training_synchronization("bend", "bend"))
'''
6,4
'''