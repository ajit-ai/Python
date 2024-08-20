def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def bubble_sort_modified(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sorted(input_array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(input_array)):
            if input_array[i - 1] > input_array[i]:
                input_array[i], input_array[i - 1] = input_array[i - 1], input_array[i]
                swapped = True
    return input_array

if __name__ == "__main__":
    # 1. Call bubble_sort(array) function
    array = [11, 14, 3, 8, 18, 17, 43]
    print("Bubble sort call bubble_sort(array): ", bubble_sort(array))

    # 2. Call bubble_sort_modified(arr) function
    arr = [64, 25, 12, 22, 11]
    bubble_sort_modified(arr)
    print("Bubble Sorted call bubble_sort_modified(arr): ", arr)

    # 3. Call bubble_sorted(input_array) function
    unsorted = [10, 6, 2, 1, 5, 8, 3, 4, 7, 9]
    sorted_array = bubble_sorted(unsorted)
    print("Bubble Sorted call bubble_sorted(input_array): ", sorted_array)