"""
Elias γ code or Elias gamma code is a universal code
encoding positive integers.
It is used most commonly when coding integers whose
upper-bound cannot be determined beforehand.
Elias δ code or Elias delta code is a universal code
 encoding the positive integers,
that includes Elias γ code when calculating.
Both were developed by Peter Elias.

"""

import math

def elias_gamma_encode(n):
    """Encode a positive integer using Elias Gamma coding."""
    if n <= 0:
        raise ValueError("Elias Gamma encoding is for positive integers only")
    
    # Calculate binary representation without '0b' prefix
    binary = bin(n)[2:]
    L = len(binary) - 1
    
    # Prefix with L zeros followed by binary representation
    code = '0' * L + binary
    return code

def elias_gamma_decode(code):
    """Decode an Elias Gamma coded string to a positive integer."""
    if not code:
        raise ValueError("Empty code string")
    
    # Count leading zeros
    L = 0
    while L < len(code) and code[L] == '0':
        L += 1
    
    # Read next L+1 bits as binary number
    if L + L + 1 > len(code):
        raise ValueError("Invalid Elias Gamma code")
    
    binary_part = code[L:L + L + 1]
    return int(binary_part, 2)

def elias_delta_encode(n):
    """Encode a positive integer using Elias Delta coding."""
    if n <= 0:
        raise ValueError("Elias Delta encoding is for positive integers only")
    
    # Calculate binary representation of n
    binary = bin(n)[2:]
    L = len(binary)
    
    # Encode L using Elias Gamma
    gamma_part = elias_gamma_encode(L)
    
    # Append binary of n without the leading 1
    binary_part = binary[1:] if len(binary) > 1 else ''
    
    return gamma_part + binary_part

def elias_delta_decode(code):
    """Decode an Elias Delta coded string to a positive integer."""
    if not code:
        raise ValueError("Empty code string")
    
    # First decode the gamma part to get L
    L = 0
    while L < len(code) and code[L] == '0':
        L += 1
    
    if L + L + 1 > len(code):
        raise ValueError("Invalid Elias Delta code")
    
    # Get the binary length (L) using gamma decoding
    gamma_length = L + L + 1
    binary_L = code[L:gamma_length]
    L_value = int(binary_L, 2)
    
    # Read the remaining bits as the binary number (excluding leading 1)
    binary_part = '1' + code[gamma_length:gamma_length + L_value - 1]
    return int(binary_part, 2)

# Example usage
if __name__ == '__main__':
    test_numbers = [1, 4, 13]
    
    print("Elias Gamma Coding:")
    for n in test_numbers:
        encoded = elias_gamma_encode(n)
        decoded = elias_gamma_decode(encoded)
        print(f"Number: {n}, Gamma Encoded: {encoded}, Decoded: {decoded}")
    
    print("\nElias Delta Coding:")
    for n in test_numbers:
        encoded = elias_delta_encode(n)
        decoded = elias_delta_decode(encoded)
        print(f"Number: {n}, Delta Encoded: {encoded}, Decoded: {decoded}")