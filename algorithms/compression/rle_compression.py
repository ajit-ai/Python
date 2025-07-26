"""
Run-length encoding (RLE) is a simple compression algorithm 
that gets a stream of data as the input and returns a
sequence of counts of consecutive data values in a row.
When decompressed the data will be fully recovered as RLE
is a lossless data compression.
"""

def encode_rle(input):
    """
    Gets a stream of data and compresses it
    under a Run-Length Encoding.
    :param input: The data to be encoded.
    :return: The encoded string.
    """
    if not input: return ''

    encoded_str = ''
    prev_ch = ''
    count = 1

    for ch in input:

        # Check If the subsequent character does not match
        if ch != prev_ch:
            # Add the count and character
            if prev_ch:
                encoded_str += str(count) + prev_ch
            # Reset the count and set the character
            count = 1
            prev_ch = ch
        else:
            # Otherwise increment the counter
            count += 1
    else:
        return encoded_str + (str(count) + prev_ch)


def decode_rle(input):
    """
    Gets a stream of data and decompresses it
    under a Run-Length Decoding.
    :param input: The data to be decoded.
    :return: The decoded string.
    """
    decode_str = ''
    count = ''

    for ch in input:
        # If not numerical
        if not ch.isdigit():
            # Expand it for the decoding
            decode_str += ch * int(count)
            count = ''
        else:
            # Add it in the counter
            count += ch
    return decode_str


#call main method to get result
if __name__ == '__main__':
    print(encode_rle('AAAABBBCCDAA'))
    print(decode_rle('4A3B2C1D2A'))
    print(encode_rle(''))
    print(decode_rle(''))
    print(encode_rle('A'))
    print(decode_rle('1A'))
    print(encode_rle('AA'))
    print(decode_rle('2A'))