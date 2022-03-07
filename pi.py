#Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. 
#Keep a limit to how far the program will go.

import math

def round_pi():
    
    n = int(input("number of playces: "))
    
    if n < 10:
        return round(math.pi,n)
    else:
        print("number is to big, plese get lower" + round_pi())
