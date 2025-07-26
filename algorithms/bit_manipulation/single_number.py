"""
Given an array of integers, every element appears
twice except for one. Find that single one.

NOTE: This also works for finding a number occurring odd
      number of times, where all the other numbers appear
      even number of times.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
def single_number(nums):
    """
    Returns single number, if found.
    Else if all numbers appear twice, returns 0.
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
        i ^= num
    return i


#call main method to get result
if __name__ == '__main__':
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([2, 2, 1]))
    print(single_number([1]))
    print(single_number([0]))
    print(single_number([1, 1]))
    print(single_number([2, 1, 2]))