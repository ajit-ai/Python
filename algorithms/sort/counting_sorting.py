def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    return [i for i in range(len(count)) for _ in range(count[i])]

arr = [1, 4, 1, 2, 7, 5, 2]
max_val = max(arr)
sorted_arr = counting_sort(arr, max_val)
print(sorted_arr)