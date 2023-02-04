x: int = 0

while(x<=1):
    print(chr(129312))
    x=x+1

"""practice"""
x = 1
y = 2
z = "x"

if x>y:
    print(str(x))
else:
    if y % 2 == 0:
        print(str(y))
print(z)

"""A tracing practice question"""
i: int = 0
s: str = ""
while i<4:
    if i % 2 ==0:
        s = s +"h"
    else:
        if i % 3 == 0:
            s = s +"!"
        else:
            s = s + "e"
    i = i + 1

print(i)
print(s)


'''Writing Code in class: Guessing game'''
"""Asks user for their number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True
number_of_guesses = 1

while playing:
    if number_of_guesses < 4:
        playing = False
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else:
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd, the answer is even")
        if guess > SECRET:
            print("Your guess is too high! ")
        else: #guess < SECRET
            print("Your guess is too low ")
        guess = int(input("Make another guess! "))
    number_of_guesses = number_of_guesses +1

print("Number of guesses " + str(number_of_guesses))