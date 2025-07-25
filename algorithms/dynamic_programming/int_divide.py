"""
Given positive integer decompose, find an algorithm to find the number of
non-negative number division, or decomposition.

The complexity is O(n^2).

Example 1:
Input: 4
Output: 5
Explaination:
4=4
4=3+1
4=2+2
4=2+1+1
4=1+1+1+1

Example :
Input: 7
Output: 15
Explaination:
7=7
7=6+1
7=5+2
7=5+1+1
7=4+3
7=4+2+1
7=4+1+1+1
7=3+3+1
7=3+2+2
7=3+2+1+1
7=3+1+1+1+1
7=2+2+2+1
7=2+2+1+1+1
7=2+1+1+1+1+1
7=1+1+1+1+1+1+1

"""


def int_divide(decompose):
    """Find number of decompositions from `decompose`

    decompose -- integer
    """
    arr = [[0 for i in range(decompose + 1)] for j in range(decompose + 1)]
    arr[1][1] = 1
    for i in range(1, decompose + 1):
        for j in range(1, decompose + 1):
            if i < j:
                arr[i][j] = arr[i][i]
            elif i == j:
                arr[i][j] = 1 + arr[i][j - 1]
            else:
                arr[i][j] = arr[i][j - 1] + arr[i - j][j]
    return arr[decompose][decompose]

#call main method
if __name__ == '__main__':
    print(int_divide(4))
    print(int_divide(7))
    print(int_divide(10))

