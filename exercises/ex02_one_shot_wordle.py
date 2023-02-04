"""Ex02 - One Shot Wordle"""
__author__ = "730412085"

secret: str = "python"
len_secret: int = len(secret)
guess: str = input(f"What is your {len_secret}-letter guess? ")
index: int = 0
numb_guess: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result = str()
"""Whether a letter in a guess should have a yellow box"""
yellow_check: int = 0
"""What the yellow/white box loop runs on"""
color_bool: bool = False

"""To make sure guess is x letters, with each mistake guess count goes up until a maximum of 4 guesses"""
while(len(guess) != len_secret):
    if(numb_guess < 4):
        guess = input(f"That was not {len_secret} letters! Try again: ")
        numb_guess = numb_guess + 1
    else:
        print("Not quite. Play again soon!")
        exit()

"""Guess is x letters, so output respective colored boxes"""
while(index < len_secret):
    yellow_check = 0
    color_bool = False
    if(guess[index] == secret[index]):
        result = (f"{result}{GREEN_BOX}")
        index = index+1
    else:
        while(color_bool == False):
            while(yellow_check < len_secret):
                if(guess[index] == secret[yellow_check]):
                    color_bool = True
                    yellow_check = len_secret
                    result = (f"{result}{YELLOW_BOX}")
                    index = index + 1
                else:
                    yellow_check = yellow_check + 1
                    if(yellow_check == len_secret):
                        color_bool = True
            result = (f"{result}{WHITE_BOX}")      
            index = index + 1

"""Reset variables"""
yellow_check = 0
color_bool = False

"""Results: if guess is correct all green boxes, if incorrect green/yellow/white boxes with corresponding notes"""
if(guess == secret):
        print(f"{result} \nWoo you got it!")
        exit()
else:
        print(f"{result} \nNot quite. Play again soon!")
        exit()