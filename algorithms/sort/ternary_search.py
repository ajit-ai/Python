def ternary_search(arr, l, r, x):
    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == x: return mid1
        if arr[mid2] == x: return mid2
        if arr[mid1] > x: r = mid1 - 1
        elif arr[mid2] < x: l = mid2 + 1
        else: l, r = mid1 + 1, mid2 - 1
    return -1
# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    x = 70
    result = ternary_search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")