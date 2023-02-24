"""Developing Utility Functions using lists."""
__author__ = "7304121085"


def all(utils_list: list[int], input_int: int) -> bool:
    """Takes a list and compares each item in list to some singular integer."""
    utils_idx = 0
    
    if (len(utils_list) == 0):
        return (False)
    while (utils_list[utils_idx] == input_int):
        utils_idx += 1
        if (utils_idx > len(utils_list) - 1):
            return (True)
    return (False)


def max(max_list: list[int]) -> int:
    """Finds maximum number within a list."""
    max_int = max_list[0]
    max_idx = 0

    if (len(max_list) == 0):
        raise ValueError("max() arg is an empty List")
    while (max_idx <= len(max_list) - 1):
        if (max_list[max_idx] > max_int):
            max_int = max_list[max_idx]
            max_idx += 1
        else:
            max_idx += 1
    return (max_int)


def is_equal(first_equal: list[int], second_equal: list[int]) -> bool:
    """Compares two lists and outputs a boolean depending on whether they are identical or not."""
    e_idx = 0
    if (len(first_equal) == len(second_equal)):
        while (e_idx <= len(first_equal) - 1):
            if (first_equal[e_idx] == second_equal[e_idx]):
                e_idx += 1
            else:
                return (False)
        return (True)
    else:
        return (False)