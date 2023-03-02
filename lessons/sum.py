"""Example function for unit tests. Uses for rather than while."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for num in xs:
        sum_total += num
    return sum_total