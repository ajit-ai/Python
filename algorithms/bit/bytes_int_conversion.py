from collections import deque


# want into to byte big endian by number hex and decode to handel
def int_to_bytes_big_endian(hex_num):
    return bytes.fromhex(hex_num)[::-1]

# want into to byte little endian by number hex and decode to handel
def int_to_bytes_little_endian(decode):
    return bytes.fromhex(decode)[::-1]

def bytes_big_endian_to_int(decode):
    return int.from_bytes(decode, 'big')

def bytes_little_endian_to_int(decode):
    return int.from_bytes(decode, 'little')
    

def int_to_bytes_big_endian(num):
    bytestr = deque()
    while num > 0:
        # list.insert(0, ...) is inefficient
        bytestr.appendleft(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def int_to_bytes_little_endian(num):
    bytestr = []
    while num > 0:
        bytestr.append(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def bytes_big_endian_to_int(bytestr):
    num = 0
    for b in bytestr:
        num <<= 8
        num += b
    return num

def bytes_little_endian_to_int(bytestr):
    num = 0
    e = 0
    for b in bytestr:
        num += b << e
        e += 8
    return num


#call main 
if __name__ == '__main__':
    print(int_to_bytes_big_endian(123))
    print(int_to_bytes_little_endian(123))
    print(bytes_big_endian_to_int(b'\x00\x7b'))
    print(bytes_little_endian_to_int(b'\x7b\x00'))

    print(int_to_bytes_big_endian(123).hex())
    print(int_to_bytes_little_endian(123).hex())
    #print(bytes_big_endian_to_int(b'\x00\x7b').hex())
    #print(bytes_little_endian_to_int(b'\x7b\x00').hex())
    
    print(int_to_bytes_big_endian(123).decode())
    print(int_to_bytes_little_endian(123).decode())
    #print(bytes_big_endian_to_int(b'\x00\x7b').decode())
    #print(bytes_little_endian_to_int(b'\x7b\x00').decode())