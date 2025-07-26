"""A Dynamic Programming solution for Rod cutting problem
"""
def rod_cutting(n, prices):
    """
    Solve the rod cutting problem using dynamic programming.
    
    Args:
        n: Length of the rod (integer).
        prices: List of prices where prices[i-1] is the price for a rod of length i.
    
    Returns:
        Tuple of (maximum revenue, list of cut lengths).
    """
    if n <= 0 or not prices:
        return 0, []
    
    # Initialize dp array for maximum revenue
    dp = [0] * (n + 1)
    # Initialize cuts array to track the first cut length used
    cuts = [0] * (n + 1)
    
    # Compute maximum revenue for each length i
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, min(i + 1, len(prices) + 1)):
            if prices[j-1] + dp[i-j] > max_val:
                max_val = prices[j-1] + dp[i-j]
                cuts[i] = j
        dp[i] = max_val
    
    # Reconstruct the cuts
    result_cuts = []
    remaining_length = n
    while remaining_length > 0:
        cut_length = cuts[remaining_length]
        result_cuts.append(cut_length)
        remaining_length -= cut_length
    
    return dp[n], result_cuts

# Example usage
if __name__ == "__main__":
    test_cases = [
        (8, [1, 5, 8, 9, 10, 17, 17, 20]),  # Expected: 22, e.g., [2, 2, 4]
        (4, [1, 5, 8, 9]),                  # Expected: 10, e.g., [2, 2]
        (1, [1]),                           # Expected: 1, [1]
        (0, []),                            # Expected: 0, []
    ]
    
    for n, prices in test_cases:
        max_revenue, cuts = rod_cutting(n, prices)
        print(f"Rod length: {n}, Prices: {prices}")
        print(f"Maximum revenue: {max_revenue}, Cuts: {cuts}")