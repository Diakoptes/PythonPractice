#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.

def reverse_str():
    
    reverse_list = []
    reverse_string = ''
    user_string = input("give a string:\n")
    
    user_string = user_string[::-1]
    
    user_string_lst = user_string.split()
    
    for word in user_string_lst:
        reverse_list.append(word[::-1])
    
    for w in reverse_list:
        reverse_string += " " + w
    
    print(f"Reverse string:\n{reverse_string}")
