# read an user input and print it
n = int(input())

if n % 2 == 1:
    print('A')
elif n >= 2 and n <= 5:
    print('B')
elif n >= 6 and n <= 20:
    print('C')
elif n > 20:
    print('D')
elif n % 2 == 0:
    print('E')
