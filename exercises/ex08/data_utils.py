"""Functions for EX08."""


__author__ = "730412085"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dicts with header key."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8") 
    #"r" tells it to read, the last part is something you just have to add, don't worry about it
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return (result)


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return (result)


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key assign it's value as the list of those column values aka for each key make a doctionary entry with all column values
        result[key] = column_values(table, key)
    return (result)


def head(head_dict: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Creates a column-based table with only the first "n" rows of data for each column."""
    new_dict: dict[str, list[str]] = {}
    for header in head_dict:
        num_list: list[str] = []
        for elem in head_dict[header]:
            if len(num_list) < num_rows:
                num_list.append(elem)
        new_dict[header] = num_list
    return (new_dict)


def select(select_dict: dict[str, list[str]], select_list: list[str]) -> dict[str, list[str]]:
    """Creates a new column-based table with only a specific subset of the original columns."""
    new_dict: dict[str, list[str]] = {}
    for col in select_list:
        new_dict[col] = select_dict[col]
    return (new_dict)


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new column-based table with 2 column-based tables combined."""
    new_dict: dict[str, list[str]] = {}
    for key in table_1:
        new_dict[key] = table_1[key]
    for key in table_2:
        if key in new_dict:
            new_list: list[str] = list()
            for elem in new_dict[key]:
                new_list.append(elem)
            for value in table_2[key]:
                new_list.append(value)
            new_dict[key] = new_list
        else:
            new_dict[key] = table_2[key]
    return (new_dict)


def count(count_list: list[str]) -> dict[str, int]:
    """Given a list, produces a dictionary where each key is unique and each value is the count of the frequency of that value in the list."""
    new_dict: dict[str, int] = {}
    for value in count_list:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return (new_dict)