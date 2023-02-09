"""Example functions to learn definition and calling syntax"""
from random import randint

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2: 
        return number1
    else: #number1 < number2
        return number2

max_number: int = my_max(randint(1,40), randint(1,40))
print(max_number)

