def fib_search(arr, x):
    fib2, fib1, fib = 0, 1, 1
    while fib < len(arr): fib0 = fib1; fib1 = fib2; fib2 = fib1 + fib0; fib = fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)
        if arr[i] < x: fib = fib1; fib1 = fib2 - fib1; fib2 = fib
        elif arr[i] > x: fib = fib2 - fib1; fib1 = fib2 - fib1 - fib; fib2 = fib
        else: return i
        offset = i
    return 0 if arr[0] == x else -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    x = 70
    result = fib_search(arr, x)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")