"""
Get a full absolute path a file
"""
import os
def full_path(file):
    return os.path.abspath(os.path.expanduser(file))

#call main method
if __name__ == '__main__':
    print(full_path("algorithms/unix/test.py"))
    print(full_path("~algorithms/unix/test.py"))
    print(full_path("~/algorithms/unix/test.py"))
    print(full_path("/algorithms/unix/test.py"))