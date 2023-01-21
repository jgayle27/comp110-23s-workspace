"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730412085"

Ch_word: str = input("Enter a 5-character word: ")
if(len(Ch_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

Ch_letter: str = input("Enter a single character: ")
Ch_count: int = 0

print("Searching for " + Ch_letter + " in " + Ch_word)

if(Ch_letter == Ch_word[0]):
    print(Ch_letter + " found at index 0")
    Ch_count = Ch_count + 1

if(Ch_letter == Ch_word[1]):
    print(Ch_letter + " found at index 1")
    Ch_count = Ch_count + 1

if(Ch_letter == Ch_word[2]):
    print(Ch_letter + " found at index 2")
    Ch_count = Ch_count + 1

if(Ch_letter == Ch_word[3]):
    print(Ch_letter + " found at index 3")
    Ch_count = Ch_count + 1

if(Ch_letter == Ch_word[4]):
    print(Ch_letter + " found at index 4")
    Ch_count = Ch_count + 1


if(Ch_count == 0):
    print("No instances of " + Ch_letter + " found in " + Ch_word)
if(Ch_count == 1):
    print("1 instance of " + Ch_letter + " found in " + Ch_word)
if(Ch_count > 1):
    Ch_count =str(Ch_count)
    print(Ch_count + " instances of " + Ch_letter + " found in " + Ch_word)

