class Fibonacci:
    @staticmethod
    def main(args):
        # fibonnaci serise
        n = 10  # Example input for Fibonacci series length
        fib_series = [0] * n
        fib_series[0] = 0  # First Fibonacci number
        if n > 1:
            fib_series[1] = 1  # Second Fibonacci number
        for i in range(2, n):
            fib_series[i] = fib_series[i - 1] + fib_series[i - 2]  # Calculate the next Fibonacci number
        print("Fibonacci Series:")
        for i in range(n):
            print(fib_series[i], end=" ")  # Print the Fibonacci series

Fibonacci.main([])