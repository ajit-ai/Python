"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192
(represented in binary as 00111001011110000010100101000000).
"""
def reverse_bits(n):
    m = 0
    i = 0
    while i < 32:
        m = (m << 1) + (n & 1)
        n >>= 1
        i += 1
    return m

#call main method to get result
if __name__ == '__main__':
    print(reverse_bits(43261596))
    print(bin(43261596))
    print(bin(964176192))
    print(bin(reverse_bits(43261596)))
    print(bin(reverse_bits(964176192)))
    print(reverse_bits(964176192))
    print(reverse_bits(43261596))