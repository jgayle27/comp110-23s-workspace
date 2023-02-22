"""EX03 - Structured Wordle."""
__author__ = "730412085"


def contains_char(secret: str, guess_char: str) -> bool:
    """Compares the secret's letters to the guess's letters and outputs a boolean value."""
    assert len(guess_char) == 1
    secret_char_count = 0
    contains_var: bool = False
    """Assess letters"""
    while (secret_char_count < len(secret) and contains_var is False): 
        if (guess_char == secret[secret_char_count]): 
            contains_var = True
        else:
            if (guess_char != secret[secret_char_count]): 
                secret_char_count = secret_char_count + 1
    return(contains_var)

                        

def emojified(guess: str, secret: str) -> str:
    """Output colored boxes according to correctness and limited by secret length."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result = str()
    guess_index = 0

    """Select box for each character and add to result string."""
    while (guess_index < len(secret)):
        if (contains_char(secret, guess[guess_index]) is True):
            if (guess[guess_index] == secret[guess_index]):
                result = (f"{result}{GREEN_BOX}")
            else:
                result = (f"{result}{YELLOW_BOX}")
        else:
            result = (f"{result}{WHITE_BOX}")
        guess_index = guess_index + 1
    return (result)


def input_guess(number_letters: int) -> str:
    """Takes length of the secret and ensures the guess is the same length, outputs guess."""
    guess = input(f"Enter a {number_letters} character word: ")
    while (len(guess) != number_letters):
        guess = input(f"That wasn't {number_letters} chars! Try again: ")
    return (guess)
    

def main() -> None:
    """The entry point of the program and main game loop."""
    """Variables needed."""
    N: int = 1
    secret: str = "codes"
    exit: bool = False

    while (exit is False):
        print(f"=== Turn {N}/6 ===")
        main_guess = input_guess(len(secret))
        print(emojified(main_guess, secret))
        if (main_guess == secret):
            print(f"You won in {N}/6 turns!")
            exit = True
        else:
            if (N == 6):
                print("X/6 - Sorry, try again tomorrow!")
                exit = True
            N = N + 1
        

if __name__ == "__main__":
    main()