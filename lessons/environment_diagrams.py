"""Example environment diagram program."""

age: int = 20
year: int = 2023
age_in_2043: int = 2043 - year +age
print("In 2043, you'll be " + str(age_in_2043))


age = age +1
year = year +1
print("In " +str(year) + ", you'll be " + str(age))

"""Example environment diagram program with conditionals"""
secret:  int = 3
guess: int = 1

if guess == secret:
    print("Success!")
    print(str(guess) +" is the secret number!")
else:
    guess = guess + 1
    if guess ==secret:
        print("Success on 2nd try!")
    else: 
        print("Wrong guess. :(")
        if (guess == secret - 1):
            print("The guess of " + str(guess) + " is off by only one number!")