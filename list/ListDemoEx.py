class Demo:
    @staticmethod
    def main(args):
        """
        Prints 1 if x is odd, 0 if x is even.
        """
        x = 17
        print(x % 2)  # Output: 1 (since 17 is odd)

if __name__ == "__main__":
    Demo.main([])