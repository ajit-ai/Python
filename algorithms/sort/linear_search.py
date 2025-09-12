def linear_search(arr, x): return next((i for i, v in enumerate(arr) if v == x), -1)

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    x = 70
    result = linear_search(arr, x)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")