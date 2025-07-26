def fact(n):

    if (n==0):
        # comment:
        return 1 
    else:
        # comment:
        return n*fact(n-1) 

#call main method

if __name__ == '__main__':
    print(fact(4))