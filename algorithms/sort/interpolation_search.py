def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high: return low if arr[low] == x else -1
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x: return pos
        if arr[pos] < x: low = pos + 1
        else: high = pos - 1
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    x = 70
    result = interpolation_search(arr, x)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")