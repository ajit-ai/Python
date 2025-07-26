""" Performs Booths algorithm returning the earliest index of the
  lexicographically smallest string rotation. Note that comparisons
  are done using ASCII values, so mixing lowercase and uppercase
  letters may give you unexpected results, O(n) """
  
  
def booth(s):
    s = s + s  # Concatenate string to itself
    n = len(s)
    f = [-1] * n  # Failure function
    k = 0  # Least rotation of string found so far

    for j in range(1, n):
        sj = s[j]
        i = f[j - k - 1]
        while i != -1 and sj != s[k + i + 1]:
            if sj < s[k + i + 1]:
                k = j - i - 1
            i = f[i]

        if sj != s[k + i + 1]:  # Mismatch after i matches
            if sj < s[k]:  # Found a smaller rotation
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1

    return k


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bootsAlgorithms.py <string>")
        sys.exit(1)
    
    s = sys.argv[1]
    index = booth(s)
    print(f"The earliest index of the lexicographically smallest rotation of '{s}' is: {index}")