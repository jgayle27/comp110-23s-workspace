def short_words(word_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5
characters."""
    new_list: list[str] = []
    for num in word_list:
        if len(num) < 5:
            new_list.append(num)
        else:
            print(f"{num} is too long.")
    return(new_list)

list_w: list[str] = ["sun","cloud","sky"]
print(short_words(list_w))

for elem in range(1,6,2):
    print(elem)