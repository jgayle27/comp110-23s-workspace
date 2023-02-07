"""Ex02 - One Shot Wordle."""
__author__ = "730412085"

secret: str = "python"
len_secret: int = len(secret)
index: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result = str()
"""Whether a letter in a guess should have a yellow box"""
yellow_check: int = 0
"""What the yellow/white box loop runs on"""
color_bool: bool = False
guess: str = input(f"What is your {len_secret}-letter guess? ")

"""To make sure guess is x letters"""
while (len(guess) != len_secret): 
    guess = input(f"That was not {len_secret} letters! Try again: ")

"""Guess is x letters, so output respective colored boxes"""
while (index < len_secret): 
    yellow_check = 0
    color_bool = False
    if (guess[index] == secret[index]): 
        result = (f"{result}{GREEN_BOX}")
        index = index + 1
    else:
        while (color_bool is False):            
            if (guess[index] == secret[yellow_check]): 
                result = (f"{result}{YELLOW_BOX}") 
                index = index + 1
                color_bool = True
            else:
                if (guess[index] != secret[yellow_check]): 
                    yellow_check = yellow_check + 1
                    if (yellow_check >= len_secret): 
                        result = (f"{result}{WHITE_BOX}")
                        index = index + 1
                        color_bool = True

"""Results: if guess is correct all green boxes, if incorrect green/yellow/white boxes with corresponding notes"""
if (guess == secret): 
    print(f"{result} \nWoo! You got it!")
else:
    print(f"{result} \nNot quite. Play again soon!")
