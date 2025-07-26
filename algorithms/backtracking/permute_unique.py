"""
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permute_unique(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for l in perms:
            for i in range(len(l)+1):
                new_perms.append(l[:i]+[n]+l[i:])
                if i < len(l) and l[i] == n:
                    break  # handles duplication
        perms = new_perms
    return perms

# call main method to get unique permutations


if __name__ == '__main__':
    print(permute_unique([1, 1, 2]))