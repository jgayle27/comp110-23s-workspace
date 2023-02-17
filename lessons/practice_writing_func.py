"""Practice writing a mimic funcition that returns a string"""
from random import randint


def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("hello!")
print(mimic("hello!"))

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if(len(my_words) <= letter_idx):
        return("Too high of an index")
    else:
        return(my_words[letter_idx])

print(mimic_letter("What up", randint(0,5)))

