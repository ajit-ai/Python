def bucket_sort(arr):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        idx = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        buckets[idx].append(num)
    result = []
    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)
    return result
