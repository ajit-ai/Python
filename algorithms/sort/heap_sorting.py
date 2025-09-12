import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
# Example
arr = [64, 34, 25, 12, 22, 11]
print(heap_sort(arr))