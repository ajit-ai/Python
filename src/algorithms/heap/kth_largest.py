def kth_largest(nums, k):
    import heapq
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0] if min_heap else None


def kth_largest_sort(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1] if k <= len(nums) else None
