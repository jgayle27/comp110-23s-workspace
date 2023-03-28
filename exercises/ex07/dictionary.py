"""Ex07 - Dictionary Functions."""

__author__ = "730412085"

def invert (i_dict: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = i_dict
    for elem in i_dict:
        elem = i_dict[elem]
        i_dict[elem] = i_dict[elem]
    print(i_dict)
    for elem in new_dict:
        new_dict[elem] = i_dict[elem]
    print(new_dict)

invert({"a":"!","b":"2","c":"3"})
        
