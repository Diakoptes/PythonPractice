#Write a program that returns a list that contains only the 
#elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

import random
randomlist = []
randomlist_1 = []

for i in range(0,8):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)

for j in range(0,10):
    m = random.randint(1,30)
    randomlist_1.append(m)
print(randomlist_1)

common_set = set(randomlist + randomlist_1)
common_set
