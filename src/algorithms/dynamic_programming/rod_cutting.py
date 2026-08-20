def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    return dp[n]
