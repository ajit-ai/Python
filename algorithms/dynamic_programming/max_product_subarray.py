"""
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
from functools import reduce


def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lmin = lmax = gmax = nums[0]
    for num in nums:
        t_1 = num * lmax
        t_2 = num * lmin
        lmax = max(max(t_1, t_2), num)
        lmin = min(min(t_1, t_2), num)
        gmax = max(gmax, lmax)


"""
Another approach that would print max product and the subarray

Examples:
subarray_with_max_product([2,3,6,-1,-1,9,5])
    #=> max_product_so_far: 45, [-1, -1, 9, 5]
subarray_with_max_product([-2,-3,6,0,-7,-5])
    #=> max_product_so_far: 36, [-2, -3, 6]
subarray_with_max_product([-4,-3,-2,-1])
    #=> max_product_so_far: 24, [-4, -3, -2, -1]
subarray_with_max_product([-3,0,1])
    #=> max_product_so_far: 1, [1]
"""


def subarray_with_max_product(arr):
    ''' arr is list of positive/negative numbers '''
    length = len(arr)
    product_so_far = max_product_end = 1
    max_start_i = 0
    so_far_start_i = so_far_end_i = 0
    all_negative_flag = True

    for i in range(length):
        max_product_end *= arr[i]
        if arr[i] > 0:
            all_negative_flag = False

        if max_product_end <= 0:
            max_product_end = arr[i]
            max_start_i = i

        if product_so_far <= max_product_end:
            product_so_far = max_product_end
            so_far_end_i = i
            so_far_start_i = max_start_i

    if all_negative_flag:
        print(f"max_product_so_far: {reduce(lambda x, y: x * y, arr)}, {arr}")

    else:
        print(f"max_product_so_far: {product_so_far},{arr[so_far_start_i:so_far_end_i + 1]}")


# Test
subarray_with_max_product([2, 3, 6, -1, -1, 9, 5])
subarray_with_max_product([-2, -3, 6, 0, -7, -5])
subarray_with_max_product([-4, -3, -2, -1])
subarray_with_max_product([-3, 0, 1])