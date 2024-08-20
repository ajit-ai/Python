import mmap
# Memory-mapping a file
with open("data.txt", "r+b") as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)
    print(mmapped_file.readline())
    mmapped_file.close()