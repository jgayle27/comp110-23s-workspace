"""Ex05 - Utils."""
__author__ = "730412085"


def only_evens(evens_list: list[int]) -> list:
    """Takes given list and returns a list with only even numbers from original list."""
    end_list: list[int] = list()
    elem: int = 0
    for elem in evens_list:
        if elem % 2 == 0:
            end_list.append(elem)
    return (end_list)


def concat(list_a: list[int], list_b: list[int]) -> list:
    """Takes two lists and puts the first in front of the second in new list."""
    new_list = ()
    new_list = list_a
    for idx in list_b:
        new_list.append(idx)
    return (new_list)


def sub(sub_list: list[int], st_idx: int, end_idx: int) -> list:
    """Takes a list and uses a start and end index to takes only a certain section of the list."""
    new_sub_list: list[int] = list()

    if st_idx < 0:
        st_idx = -st_idx
    if st_idx == len(sub_list):
        return (new_sub_list)
    if end_idx < 0:
        end_idx = -end_idx
    if end_idx > len(sub_list) - 1:
        end_idx = len(sub_list) - 1
    if len(sub_list) == 0:
        return (new_sub_list)

    for st_idx in sub_list:
        new_sub_list.append(st_idx)
        if st_idx > end_idx:
            return (new_sub_list)