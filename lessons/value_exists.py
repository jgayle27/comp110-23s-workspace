def value_exists(value_dict: dict[str,int], num: int) -> bool:

    for elem in value_dict:
        if (value_dict[elem] == num):
            return(True)
    return(False)
        
