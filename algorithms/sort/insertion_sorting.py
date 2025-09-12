def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def insertion_sort(arr, simulation=False):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)
            
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr, simulation=True)
    print("Sorted array:", sorted_arr)