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
    new_list: list[int] = list()
    for idx_a in list_a:
        new_list.append(idx_a)
    for idx_b in list_b:
        new_list.append(idx_b)
    return (new_list)


def sub(sub_list: list[int], st_idx: int, end_idx: int) -> list:
    """Takes a list and uses a start and end index to take only a certain section of the list."""
    new_sub_list: list[int] = list()

    if st_idx < 0:
        st_idx = 0
    if st_idx >= len(sub_list):
        return (new_sub_list)
    if end_idx < 0:
        end_idx = -end_idx
    if end_idx == 0:
        return (new_sub_list)
    if end_idx > len(sub_list):
        end_idx = len(sub_list)
    if len(sub_list) == 0:
        return (new_sub_list)

    for elem in sub_list:
        idx = elem + st_idx
        if idx > end_idx:
            return (new_sub_list)
        else:
            new_sub_list.append(idx)