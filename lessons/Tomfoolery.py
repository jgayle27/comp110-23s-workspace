msg: str = input("Your friend sends you a picture of their cat, how do you reply? ")
exclamation: str = "!"
index: int = 0

while (msg[index] != exclamation):
    index = index +1
    if ((msg[index] != exclamation) == False):
        print(f"Thanks! {chr(129312)}")
    if ((msg[index] != exclamation) == True):
        print("Wow you're so enthusiastic.")

