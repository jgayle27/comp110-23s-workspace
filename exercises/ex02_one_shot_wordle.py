"""Ex02 - One Shot Wordle"""
__author__ = "730412085"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
index: int = 0
sindex: int = 0
numb_guess: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result = str()

"""Make sure guess is 6 letters, with each mistake guess count goes up"""
while(len(guess) != 6):
    if(numb_guess < 4):
        guess = input("That was not 6 letters! Try again: ")
        numb_guess = numb_guess + 1
    else:
        print("Not quite. Play again soon!")
        exit()

"""guess is 6 letters, so test boxes"""
if(len(guess) == 6):
    while(index < len(secret)):
        if(guess[index] == secret[index]):
            result = (f"{result}{GREEN_BOX}")
            index = index+1
        else:
            result = (f"{result}{WHITE_BOX}")
            index = index+1

"""Results: if guess is correct green boxes, if incorrect green/white boxes"""
if(guess == secret):
        print(f"{result} \nWoo you got it!")
        exit()
else:
        print(f"{result} \nNot quite. Play again soon!")
        exit()

#while(guess[index] != secret[sindex]):
#    index = index + 1
exit()

#python -m exercises.ex02_one_shot_wordle