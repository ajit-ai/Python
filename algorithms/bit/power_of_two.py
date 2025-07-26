"""
given an integer, write a function to determine if it is a power of two
"""
def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and not n & (n-1)


#call main method to get result


if __name__ == '__main__':
    print(is_power_of_two(16))
    print(is_power_of_two(15))
    print(is_power_of_two(0))