"""Ex07 - Dictionary Functions."""


__author__ = "730412085"


def invert(i_dict: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary of strings and switches the keys and values and then outputs a dictionary of these switched keys as values and values as keys."""
    invert_list: list[str] = []
    new_dict: dict[str, str] = {}
    idx: int = 0
    check: int = idx
    while idx < len(i_dict):
        for key in i_dict:
            while check < len(invert_list):
                if i_dict[key] == invert_list[check]:
                    raise KeyError("cannot have identical keys!")
                check += 1
            check = 0
            invert_list.append(i_dict[key])
            new_dict[invert_list[idx]] = key
            idx += 1
    return (new_dict)
        

def favorite_color(color_dict: dict[str, str]) -> str:
    """Takes a dictionary of keys and corresponding color values and then tallies which colors recieve the most number of "votes" and then outputs a single str of the top-rated color (if colors are "voted" equally it outputs the first color of the dictionary from that list of equivalent appearances of colors)."""
    color_count: int = 0
    new_dict: dict[str, int] = {}
    color_list: list[str] = []
    top_color: str = ""
    test_idx: int = 0
    for key in color_dict:
        new_dict[color_dict[key]] = 0
        color_list.append(color_dict[key])
    for key in color_list:
        if key == color_list[color_count]:
            new_dict[key] += 1
        color_count += 1
    for key in new_dict:
        dict_value = new_dict[key]
        if dict_value > test_idx:
            top_color = key
            test_idx = dict_value
    return (top_color)


def count(count_list: list[str]) -> dict[str, int]:
    """Takes a list of strings and counts how many times that string is found. Count then takes those strings and the number of appearances and puts them into a dictionary where the strings are the keys and the number of appearances are the int values."""
    new_dict: dict[str, int] = {}
    for elem in count_list:
        if elem in new_dict:
            new_dict[elem] += 1
        if elem not in new_dict:
            new_dict[elem] = 1
    return (new_dict)