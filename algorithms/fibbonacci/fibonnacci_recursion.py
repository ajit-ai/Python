def nth_fibonacci(n):
  
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
      
    # Recursive case: sum of the two preceding Fibonacci numbers
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

n = 5
result = nth_fibonacci(n)
print(result)

#[Naive Approach] Using Recursion
#We can use recursion to solve this problem because any Fibonacci number n depends on previous two Fibonacci numbers. 
#Therefore, this approach repeatedly breaks down the problem until it reaches the base cases.
# Two segment as first talk about first two number and second phase is rest of all 
# F(n) = F(n-1) + F(n-2)
# Base Case: F(0) = 0, F(1) = 1
# Time Complexity: O(2n)
# Auxiliary Space: O(n), due to recursion stack