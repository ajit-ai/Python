def max_product_subarray(nums):
    if not nums:
        return 0
    max_prod = min_prod = result = nums[0]
    for i in range(1, len(nums)):
        val = nums[i]
        if val < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(val, max_prod * val)
        min_prod = min(val, min_prod * val)
        result = max(result, max_prod)
    return result
