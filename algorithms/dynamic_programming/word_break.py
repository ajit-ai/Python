"""
Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words,
determine if word can be segmented into a space-separated
sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
word = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

word = abc word_dict = ["a","bc"]
True False False False

"""

def wordBreak(s, wordDict):
    """
    Determine if string s can be segmented into words from wordDict.
    
    Args:
        s: Input string to be segmented.
        wordDict: List of words to use for segmentation.
    
    Returns:
        bool: True if s can be segmented, False otherwise.
    """
    # Convert wordDict to set for O(1) lookup
    word_set = set(wordDict)
    n = len(s)
    
    # dp[i] represents whether s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always segmentable
    
    # Check each substring ending at i
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    test_cases = [
        ("leetcode", ["leet", "code"]),  # Expected: True
        ("abc", ["a", "bc"]),           # Expected: True
        ("applepenapple", ["apple", "pen"]),  # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),  # Expected: False
    ]
    
    for s, wordDict in test_cases:
        result = wordBreak(s, wordDict)
        print(f"String: {s}, WordDict: {wordDict}, Can segment: {result}")