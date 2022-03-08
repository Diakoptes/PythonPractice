#Take a list, and write a program that prints out all the elements of the list that are less than 10.

#Extras:
#1.Instead of printing the elements one by one, make a new list that has all 
#the elements less than 10 from this list in it and print out this new list.
  
#2.Write this in one line of Python.

#3.Ask the user for a number and return a list that contains only elements from the original 
#list a that are smaller than that number given by the user.

1.
lst = list(range(0,50,3))
print(lst)

for l in lst:
    if l<10:
        print(l)
        
2.
new_lst = []

for l in lst:
    if l<10:
        new_lst.append(l)
print(new_lst)

3.
def your_numbers():

    new_lst = []
    
    num = int(input("give me a number: "))
    
    for l in lst:
        if l<num:
            new_lst.append(l)
    print(new_lst)
your_numbers()
