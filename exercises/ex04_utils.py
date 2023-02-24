"""Developing Utility Functions using lists"""
__author__ = "7304121085"

from random import randint

utils_list: list[str] = list()
int = randint(1,3)

def all(utils_list: list[int],int) -> bool:
    while(utils_list[i] == int):
        i = i + 1
        if(i > len(utils_list)):
            return(True)
    return(False)

def max(utils_list: list[int]) -> int:
    max_int = utils_list[0]
    idx = 0

    if len(utils_list) == 0:
        raise ValueError("max() arg is an empty List")
    while(idx <= len(utils_list) - 1):
        if utils_list[idx] > max_int:
            max_int = utils_list[idx]
            idx = idx + 1
        else:
            idx = idx + 1
    return(max_int)


def is_equal(first_equal: list[int], second_equal: list[int]) -> bool:
    e_idx = 0
    if(len(first_equal) == len(second_equal)):
        while(first_equal[e_idx] == second_equal[e_idx] and e_idx <= len(first_equal) - 1):
            e_idx = e_idx + 1
        return(True)
    else:
        return(False)

