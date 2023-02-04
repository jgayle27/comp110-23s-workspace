msg: str = input("Your friend sends you a picture of their cat, how do you reply? ")
exclamation: str = "!"
index: int = 0

while (msg[index] != exclamation):
    index = index +1
    if ((msg[index] != exclamation) == False):
        print(f"Thanks! {chr(129312)}")
    if ((msg[index] != exclamation) == True):
        print("Wow you're so enthusiastic.")

"""To make sure guess is x letters, with each mistake guess count goes up until a maximum of 4 guesses"""
"""while(len(guess) != len_secret):
    if(numb_guess < 4):
        guess = input(f"That was not {len_secret} letters! Try again: ")
        numb_guess = numb_guess + 1
    else:
        print("Not quite. Play again soon!")
        exit()"""