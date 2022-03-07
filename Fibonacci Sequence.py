#Fibonacci Sequence - Enter a number and have the program generate 
#the Fibonacci sequence to that number or to the Nth number.

import math

def fibo_range_lst(last_num):
    
    return list(range(0,(last_num)))
    
def fibo_bigest(last_num):
    return int(((1/math.sqrt(5))*((1+math.sqrt(5))/2)**last_num)-((1/math.sqrt(5))*((1-math.sqrt(5))/2)**last_num))
        
def main():
    
    num = int(input("num: "))
    
    range_lst = fibo_range_lst(num)
    bigest = fibo_bigest(num-1)
    fibo_numbers_lst = []
    
    if 0 in range_lst:
        fibo_numbers_lst.append(0)
        
    if 1 in range_lst:
        fibo_numbers_lst.append(1)
    
    while bigest > fibo_numbers_lst[-1]:
        fibo_numbers_lst.append(sum(fibo_numbers_lst[-2::]))
    print(bigest)   
    print(fibo_numbers_lst)
        
if __name__ == "__main__":
    main()
