def least_rotation(s: str) -> int:
    """
    Find the index of the lexicographically smallest rotation of string s.
    Uses Booth's algorithm, O(n) time complexity.
    
    Args:
        s: Input string
    Returns:
        Integer index where the smallest rotation begins
    """
    # Double the string and append it to itself
    s = s + s
    n = len(s) // 2
    # Initialize failure array
    f = [-1] * (2 * n)
    k = 0  # Index of smallest rotation found so far
    
    for j in range(1, 2 * n):
        i = f[j - k - 1]
        while i != -1 and s[j] != s[k + i + 1]:
            if s[j] < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        
        if i == -1 and s[j] != s[k + i + 1]:
            if s[j] < s[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    
    return k

# Example usage
def test_least_rotation():
    test_cases = [
        "bbaaccaadd",
        "abcd",
        "aaaa",
        "baaa",
        "AaAa",
    ]
    
    for s in test_cases:
        idx = least_rotation(s)
        rotated = s[idx:] + s[:idx]
        print(f"String: {s}")
        print(f"Smallest rotation index: {idx}")
        print(f"Smallest rotation: {rotated}\n")

if __name__ == "__main__":
    test_least_rotation()