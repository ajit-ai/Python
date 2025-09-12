def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

# Function to sort an array based on a specific digit
def counting_sort_by_digit(arr, exp):
    count = [0] * 10
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        digit = (num // exp) % 10
        sorted_arr[count[digit] - 1] = num
        count[digit] -= 1
    return sorted_arr

# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print("Sorted array:", sorted_arr)
