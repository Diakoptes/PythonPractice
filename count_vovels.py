#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found.

def count_vovels():
    
    text_input = input("give me a string:\n")
    vovels = ["a", "ą", "e", "ę", "i", "o", "u", "y"]
    number_of_vovels = 0
    for v in text_input:
        if v in vovels:
            number_of_vovels+=1
    
    print(f"You have {number_of_vovels} vovels.")
