def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for num in arr:
        buckets[int(num * 10)].append(num)
    return [num for b in buckets for num in sorted(b)]
# Example usage
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)