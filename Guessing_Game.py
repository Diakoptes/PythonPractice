import random 

def guessing_game():
    
    
    guess = random.randrange(1, 100)
    playing = True
    posibilities = list(range(0,101))
    start = "I chose a numeber.\nIt's in range 1-100."
    
    print(start)
    
    while playing:
        
        your_guess = input("What number has been chosen: ")
        
        if your_guess == "exit":
            playing = False
        
        elif your_guess.isdigit() == False or int(your_guess) not in posibilities:
            print("Chose number 1-100, or exit to close.")
        
        elif int(your_guess) < guess:
            print("Too low...")
            
        elif int(your_guess) > guess:
            print("Too high...")
            
        elif int(your_guess) == guess:
            print("Just right!")
            playing = False
