def word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]


def word_break_all(s, word_dict):
    word_set = set(word_dict)
    result = []
    _dfs(s, word_set, [], result)
    return result


def _dfs(s, word_set, path, result):
    if not s:
        result.append(list(path))
        return
    for i in range(1, len(s) + 1):
        if s[:i] in word_set:
            _dfs(s[i:], word_set, path + [s[:i]], result)
