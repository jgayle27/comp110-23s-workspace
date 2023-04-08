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
    return(result)

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return(result)

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key assign it's value as the list of those column values aka for each key make a doctionary entry with all column values
        result[key] = column_vals(table, key)
    return(result)



