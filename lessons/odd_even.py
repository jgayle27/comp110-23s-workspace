def odd_and_even(list: list[int]) -> list[int]:
    idx: int = 0
    list_2: list[int] = []
    for num in list:
        if num % 2 != 0:
            if (idx <= len(list)):
                if (idx % 2 == 0):
                    list_2.append(num)
                idx += 1
            print(list_2)


    return(list_2)
print(odd_and_even([2, 3, 4, 5]))

def better_func(list: list[int]) -> list[int]:
    idx: int = 0
    list_2: list[int] = []

    while idx < len(list):
        if list[idx] % 2 == 1 and idx % 2 == 0:
            list_2.append(list[idx])
        idx += 1
    return(list_2)

print(better_func([2, 3, 4, 5]))

        