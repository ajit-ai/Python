my_array = [15, 12, 9, 4, 11]
minVal = my_array[0]
print('minVal', minVal)

for i in my_array:
    print("Loop Min Value: ", minVal)
    if i < minVal:
        minVal = i

print('Lowest value:', minVal)