import array
import mmap

# Using fixed-length array for performance
fixed_array = array.array('i', [1, 2, 3, 4, 5])
print(fixed_array)

# Dynamic list (variable-length)
dynamic_list = [1, 2, 3, 4, 5]

print(dynamic_list)

# Memory-mapping a file
with open("data.txt", "r+b") as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)
    print(mmapped_file.readline())
    mmapped_file.close()