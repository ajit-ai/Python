def find_subarray(arr, target):
    n = len(arr)
    curr_sum = 0
    left = 0
    
    # Use sliding window technique
    for right in range(n):
        curr_sum += arr[right]
        
        # Shrink window while sum is greater than target
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1
            
        # Check if we found the target sum
        if curr_sum == target:
            # Return 1-based indices
            return [left + 1, right + 1]
    
    # No subarray found
    return [-1]


# Example usage
if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    target = 33
    result = find_subarray(arr, target)
    print(result)