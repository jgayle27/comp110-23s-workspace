"""Ex05 - Utils."""
__author__ = "730412085"


def only_evens(xs: list[int]) -> list:
    """Takes given list and returns a list with only even numbers from original list."""
    end_list: list[int] = list()
    num: int = 0
    for num in xs:
        if num % 2 == 0:
            end_list.append(num)
        num += 1
    return(end_list)


def concat(list_a: list[int], list_b: list[int]) -> list:
    """Takes two lists and puts the first in front of the second in new list."""
    new_list: list[int] = list()

    new_list.append(list_a)
    new_list.append(list_b)
    return(new_list)


def sub(sub_list: list[int], st_idx: int, end_idx: int) -> list:
    """Takes a list and uses a start and end index to takes only a certain section of the list."""
    new_sub_list: list[int] = list()

    if st_idx < 0:
        st_idx = 0
    if end_idx > len(sub_list)-1 or end_idx < 0:
        end_idx = len(sub_list)-1
    if len(sub_list) == 0:
        return(new_sub_list)
    
    for st_idx in sub_list:
        new_sub_list.append(st_idx)
        if st_idx == end_idx:
            return(new_sub_list)
        st_idx += 1