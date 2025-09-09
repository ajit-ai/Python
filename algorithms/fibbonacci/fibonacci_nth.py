# To find the n-th Fibonacci Number using by formula Fn = (φ^n - (1-φ)^n) / √5
# where φ (phi) is the golden ratio (1 + √5) / 2
from math import sqrt 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res),'is',str(n)+'th fibonacci number')
    
    
# Test the function with some inputs
nthFib(5)
nthFib(10)
nthFib(15)
nthFib(20)



