def reverse_string(s):
    buffer = list(s)
    buffer.reverse()
    return ''.join(buffer)

# Example usage
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"