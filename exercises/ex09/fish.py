"""File to define Fish class"""

class Fish:

    age: int
    
    def __init__(self):
        self.age = int(0)
    
    def __str__(self):
        """Make fish and bear lists prettier."""
        self.age = f"{self.age}"
        return None

    def one_day(self):
        self.age += 1
