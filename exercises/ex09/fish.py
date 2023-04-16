"""File to define Fish class."""


class Fish:
    """Simulate fish in river."""

    age: int
    
    def __init__(self):
        """Initialize fish ages."""
        self.age = int(0)
    
    def __str__(self):
        """Make fish and bear lists prettier."""
        self.age = f"{self.age}"
        return None

    def one_day(self):
        """Simulate fish growing one day older."""
        self.age += 1