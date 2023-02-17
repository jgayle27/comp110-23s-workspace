"""EX03 - Structured Wordle"""
__author__ = "730412085"

secret: str = "codes"
len_secret: int = len(secret)
guess_input: str = input(f"What is your {len_secret}-letter guess? ")
"""indexes guess_char and secret in function"""
guess_char_count = 0
guess_char_index = 0
guess_char: str = guess_input[guess_char_index]
"""Whether a letter in a guess should have a yellow box"""
yellow_check: int = 0
"""What the yellow/white box loop runs on"""
color_bool: bool = False

def contains_char(secret: str, guess_char: str) -> bool:
    """Compares the secret's letters to the guess's letters and outputs a boolean value"""
    assert len(guess_char) == 1

    """Assess letters"""
    while (guess_char_count < len_secret): 
        yellow_check = 0
        color_bool = False
        if (guess_char == secret[guess_char_count]): 
            guess_char_count = guess_char_count + 1
            guess_char_index = guess_char_index + 1
            return(True)
        else:
            while (color_bool is False):            
                if (guess_char == secret[yellow_check]): 
                    guess_char_index = guess_char_index + 1
                    color_bool = True
                    return(False)
                else:
                    if (guess_char != secret[yellow_check]): 
                        yellow_check = yellow_check + 1
                        if (yellow_check >= len_secret): 
                            guess_char_index = guess_char_index + 1
                            color_bool = True
                            return(False)
    guess_char_count = 0
print(contains_char)