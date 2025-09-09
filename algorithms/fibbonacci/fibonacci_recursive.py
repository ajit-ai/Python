def fibonacci(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

# Test
print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(20) = {fibonacci(20)}")
print(f"Fibonacci(30) = {fibonacci(30)}")



#import csv
#with open('input.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        n = int(row[0])
#        print(fibonacci(n))