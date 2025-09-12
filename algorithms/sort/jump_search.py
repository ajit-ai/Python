import math
def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0
    while arr[min(int(step), n) - 1] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n: return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n): return -1
    return prev if arr[prev] == x else -1

# Example usage
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 55
    result = jump_search(arr, x)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")