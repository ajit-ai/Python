def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    base = 256
    mod = 101
    h_pattern = 0
    h_text = 0
    h = 1
    for _ in range(m - 1):
        h = (h * base) % mod
    for i in range(m):
        h_pattern = (base * h_pattern + ord(pattern[i])) % mod
        h_text = (base * h_text + ord(text[i])) % mod
    results = []
    for i in range(n - m + 1):
        if h_pattern == h_text:
            if text[i:i + m] == pattern:
                results.append(i)
        if i < n - m:
            h_text = (base * (h_text - ord(text[i]) * h) + ord(text[i + m])) % mod
            if h_text < 0:
                h_text += mod
    return results
