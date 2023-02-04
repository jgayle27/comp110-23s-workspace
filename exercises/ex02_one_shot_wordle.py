"""Ex02 - One Shot Wordle"""
__author__ = "730412085"

secret: str = "python"
lensecret: int = len(secret)
guess: str = input(f"What is your {lensecret}-letter guess? ")
index: int = 0
numb_guess: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result = str()
yellow_check: int = 0
color_bool: bool = False

"""Make sure guess is x letters, with each mistake guess count goes up"""
while(len(guess) != lensecret):
    if(numb_guess < 4):
        guess = input(f"That was not {lensecret} letters! Try again: ")
        numb_guess = numb_guess + 1
    else:
        print("Not quite. Play again soon!")
        exit()

"""guess is x letters, so output boxes"""
while(index < lensecret):
    color_bool = False
    yellow_check = 0
    if(guess[index] == secret[index]):
        result = (f"{result}{GREEN_BOX}")
        index = index+1
    else:
        while(color_bool != True):
            if(guess[index] == secret[yellow_check]):
                color_bool == True
            else:
                yellow_check = yellow_check + 1
        if(color_bool == True):
            result = (f"{result}{YELLOW_BOX}")
        else: 
            result = (f"{result}{WHITE_BOX}")      
        index = index + 1
        

"""Results: if guess is correct green boxes, if incorrect green/white boxes"""
if(guess == secret):
        print(f"{result} \nWoo you got it!")
        exit()
else:
        print(f"{result} \nNot quite. Play again soon!")
        exit()

#python -m exercises.ex02_one_shot_wordle