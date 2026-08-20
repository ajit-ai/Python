def longest_palindrome_substring(s):
    if len(s) < 2:
        return s
    start, max_len = 0, 1

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        length = max(odd, even)
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2
    return s[start:start + max_len]


def longest_palindrome_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
