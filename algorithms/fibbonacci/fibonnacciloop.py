a , b = 0 , 1
nth_term = 10
count = 0
while count < nth_term:
    print(a)
    a , b = b , a + b
    count += 1
    # Test
print(f"Fibonacci sequence up to {nth_term} terms generated using loop.")
# Fibonacci sequence using loop

