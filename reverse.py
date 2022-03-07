#Reverse a String - Enter a string and the program will reverse it and print it out.


def reverse():
    
    string = str(input("Write string:" ))
    string = string[::-1]
    
    if len(string) > 1:
        print(f"This is your revers string: {string}")
        print(f"String has {len(string)} letters")
    
    elif len(string) == 1:
        print("It is a one letter")
        print(string)
    
    else:
        reverse()
