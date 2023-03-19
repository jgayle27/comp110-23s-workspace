"""Takes strings and integers in lists as arguments and returns a dictionary with str and int."""

    
def zip(a: list[str], b: list[int]) -> dict[str, int]:
    if ((a == ()) or (b == ()) or (len(a) != len(b))):
        return dict()
    else:
        result = dict()
        idx = 0
        while idx <= len(b) - 1:
            result[a[idx]] = b[idx]
            idx += 1
        return result