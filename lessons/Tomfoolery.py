"""msg: str = input("Your friend sends you a picture of their cat, how do you reply? ")
exclamation: str = "!"
index: int = 0

while (msg[index] != exclamation):
    index = index +1
    if ((msg[index] != exclamation) == False):
        print(f"Thanks! {chr(129312)}")
    if ((msg[index] != exclamation) == True):
        print("Wow you're so enthusiastic.")"""

"""To make sure guess is x letters, with each mistake guess count goes up until a maximum of 4 guesses"""
"""while(len(guess) != len_secret):
    if(numb_guess < 4):
        guess = input(f"That was not {len_secret} letters! Try again: ")
        numb_guess = numb_guess + 1
    else:
        print("Not quite. Play again soon!")
        exit()"""

def sub(sub_list: list[int], st_idx: int, end_idx: int) -> list:
    """Takes a list and uses a start and end index to takes only a certain section of the list."""
    new_sub_list: list[int] = list()

    if st_idx < 0:
        st_idx = -st_idx
        print(st_idx)
    if st_idx < 0 or st_idx == len(sub_list) - 1:
        st_idx = 0
    if end_idx > len(sub_list) - 1 or end_idx < 0:
        end_idx = len(sub_list) - 1
    if len(sub_list) == 0:
        return (new_sub_list)
    
    for st_idx in sub_list:
        new_sub_list.append(st_idx)
        if st_idx == end_idx:
            new_sub_list.append(end_idx)
            return (new_sub_list)
        
print(sub([1, 2, 3, 4], -2, 2))