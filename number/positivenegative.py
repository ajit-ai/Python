# This code is a simple console application to check if a number is positive, negative, or neither.
# Framework: Standard Python

def main():
    number_to_check = int(input("Enter the number you want to check: "))
    if number_to_check > 0:
        print("The given number " + str(number_to_check) + " is Positive")
    elif number_to_check < 0:
        print("The given number " + str(number_to_check) + " is Negative")
    else:
        print("The given number " + str(number_to_check) + " is neither Positive nor Negative")

if __name__ == "__main__":
    main()