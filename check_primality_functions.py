#Ask the user for a number and determine whether the number is prime or not.

def prime_check():
    
    divaisors = []
    num = list(range(1,1+(int(input("Num: ")))))
    max_num = max(num)
    
    for n in num:
        if max(num)%n==0:
            divaisors.append(n)
    
    if len(divaisors)>2 or max(num) == 1:
        print(f"{max(num)} it's not a prime")
    else:
        print(f"{max(num)} it's prime")
