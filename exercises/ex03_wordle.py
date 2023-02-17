"""EX03 - Structured Wordle"""
__author__ = "730412085"


"""CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
def contains_char(secret: str, guess_char: str) -> bool:
    """Compares the secret's letters to the guess's letters and outputs a boolean value"""
    assert len(guess_char) == 1
    secret_char_count = 0

    """Assess letters"""
    while (secret_char_count < len(secret)): 
        if (guess_char == secret[secret_char_count]): 
            return(True)
        else:
            if (guess_char != secret[secret_char_count]): 
                secret_char_count = secret_char_count + 1
                if (secret_char_count >= len(secret)): 
                    return(False)
                        

def emojified():
    """Output colored boxes according to correctness and secret length"""
    assert len(guess) == len(secret)

    """Assess boxes needed"""
    