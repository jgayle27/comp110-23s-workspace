"""Using for...in range(len(xs))."""

xs: list[int] = [0,1,2,3,4,5]
for digit in range(len(xs)):
    print(digit)


def sum_for(xs: list[float]) -> float:
    """return sum of all elements in xs."""
    sum_total: float = 0.0
    for num in xs:
        sum_total += num
    return sum_total

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for num in range(0, len(xs)):
        sum_total += xs[num]
    return sum_total