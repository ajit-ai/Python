def recursive_fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# Test

print(f"Recursive Fibonacci(10) = {recursive_fibonacci(10)}")
print(f"Recursive Fibonacci(20) = {recursive_fibonacci(20)}")