#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def divisor():

    divaisors = []
    
    num = list(range(1,1+(int(input("Num: ")))))
    max_num = max(num)
    
    for n in num:
        if max(num)%n==0:
            divaisors.append(n)
    print(divaisors)
