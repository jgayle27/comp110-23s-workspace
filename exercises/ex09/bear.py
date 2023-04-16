"""File to define Bear class."""


class Bear:
    """Simulate bears in river."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Initialize bear ages and hunger scores."""
        self.age = 0
        self.hunger_score = 0

    def __str__(self):
        """Print prettier version of out point."""
        self.bears = f"{self.bears}"
        return None
    
    def one_day(self):
        """Simulate change in age and hunger score for bear in one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Amount of fish bear(s) will eat in one day."""
        self.hunger_score += num_fish
        return None