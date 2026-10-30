import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}:"))
        if guess < random_number:
            print("the number you guessed is lower")
        elif guess > random_number:
            print ("the number you guessed is too high")
        
    print ("the number you guessed is correct!")



def computer_guess(x):
    low = 1 
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "H":
            


    


        

guess(10)