n = int(input())
m = int(input())
if n % 2 == 0:
    if m % 2 == 0:
        print('Even')
    else:
        print('Odd')
else:
    print('Weird')

if n % 2 == 1:
    print('Weird')
elif n >= 2 and n <= 5:
    print('Not Weird')
elif n >= 6 and n <= 20:
    print('Weird')
elif n > 20:
    print('Not Weird')