"""Ex07 - Dictionary Functions."""


__author__ = "730412085"


def invert (i_dict: dict[str, str]) -> dict[str, str]:
    invert_list: list[str] = []
    new_dict: dict[str, str] = {}
    idx: int = 0
    check: int = idx
    while idx < len(i_dict):
        for key in i_dict:
            while check < len(invert_list):
                if i_dict[key] == invert_list[check]:
                    raise KeyError("cannot have two identical keys!")
                check += 1
            check = 0
            invert_list.append(i_dict[key])
            new_dict[invert_list[idx]] = key
            idx += 1
    return(new_dict)
        

def favorite_color (color_dict: dict[str, str]) -> str:
    color_count: int = 0
    new_dict: dict[str, int] = {}
    color_list: list[str] = []
    compare_list: list[int] = []
    top_color_list: list[str] = []
    idx: int = 0
    top_color: str = ()
    #test_idx: int = 0
    for key in color_dict:
        new_dict[color_dict[key]] = 0
        color_list.append(color_dict[key])
    for key in color_list:
        if key == color_list[color_count]:
            new_dict[key] += 1
        color_count += 1
    for key in new_dict:
        compare_list.append(new_dict[key])
    #for key in new_dict:
    #    while (idx <= len(new_dict) - 1):
    #        if (new_dict[key] > compare_list[idx]):
    #            top_color = key
    #            top_color_list.append(key)
    #            print(top_color)
    #        else:
    #            idx += 1
    #    idx = 0
    for key in new_dict:
        key_bool: bool = False
        while (idx <= len(new_dict) - 1 and not key_bool):
            if (new_dict[key] >= compare_list[idx]):
                key_bool = True
                top_color = key
            if (new_dict[key] == compare_list[idx]):
                top_color_list.append(key)
                idx += 1
            else:
                idx += 1
        idx = 0
        top_color = top_color_list[0]
    return(top_color)


def count (count_list: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    for elem in count_list:
        if elem in new_dict:
            new_dict[elem] += 1
        if elem not in new_dict:
            new_dict[elem] = 1
    return(new_dict)

count_practice: list = ("cat","dog","fish","cat","fish")
print(count(count_practice))
