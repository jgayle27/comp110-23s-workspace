"""File to define River class."""

__author__ = "730412085"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Simulate a river with bears and fish."""

    day: int
    fish: list
    bears: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Copy surviving fish and bears to new list and change self.fish/bear to that list."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(Fish())
        self.fish = new_fish
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(Bear())
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Remove "amount" of fish."""
        new_fish: list[Fish] = []
        idx: int = amount
        for x in range(idx, len(self.fish)):
            new_fish.append(self.fish[x])
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Simulate bears eating and decreasing fish population."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bear if bear gets too hungry and starves."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(Bear())
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Increase number of fish in river."""
        spawn: int = (len(self.fish) // 2) * 4
        for x in range(0, spawn):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Increase number of bears in river."""
        cubs: int = len(self.bears) // 2
        for x in range(0, cubs):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Views river population stats for bears and fish according to the day."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """View one week of the simulated river of bears and fish."""
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        return None