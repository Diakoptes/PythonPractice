#Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def number(n):

    while n > 1:
    
        if n%2 == 0:
            print(n/2)
            break
    
        elif n%2 != 0:
            print((n*3) + 1)
            break
number(14)

7.0
