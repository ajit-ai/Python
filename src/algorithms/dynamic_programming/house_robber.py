def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


def house_robber_circular(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(_rob_linear(nums[:-1]), _rob_linear(nums[1:]))


def _rob_linear(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1
