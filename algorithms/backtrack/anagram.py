"""
Given two strings, determine if they are equal after reordering.

Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in s1:
        pos = ord(c)-ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c)-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2

#anagram method by value finds in true only if the strings are of same length


def anagram2(s1, s2):
    return sorted(s1) == sorted(s2)


#find anagram from the existing methods in python

if __name__ == '__main__':
    print(anagram("apple", "pleap"))
    print(anagram("apple", "cherry"))
    print(anagram2("apple", "pleap"))
    print(anagram2("apple", "cherry"))