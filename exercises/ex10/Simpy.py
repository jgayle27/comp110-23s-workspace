"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730412085"


class Simpy:
    """Simpy class which mimics 'NumPy'."""

    values: list[float]

    def __init__(self, init_list: list[float]):
        """Initialize Simpy."""
        self.values = init_list

    def __str__(self) -> str:
        """Make Simpy prettier."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, num_fill: int) -> None:
        """Fill in Simpy's values with a specific number of repeating values."""
        self.values = []
        for x in range(0, num_fill):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        if start < 0:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Find and return the sum of all items in teh values attribute."""
        sum: float = 0.0
        for x in self.values:
            sum += x
        return sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add either a float or object to the object called on."""
        add_values: Simpy = Simpy([])
        x: int = 0

        if type(rhs) == float:
            while x < len(self.values):
                add_values.values.append(self.values[x] + rhs)
                x += 1
        else: 
            assert len(self.values) == len(rhs.values)
            while x < len(self.values):
                add_values.values.append(self.values[x] + rhs.values[x])
                x += 1
        return add_values
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allow for Simpy to eval values using a power operator."""
        add_values: Simpy = Simpy([])
        x: int = 0

        if type(rhs) == float:
            while x < len(self.values):
                add_values.values.append(self.values[x] ** rhs)
                x += 1
        else: 
            assert len(self.values) == len(rhs.values)
            while x < len(self.values):
                add_values.values.append(self.values[x] ** rhs.values[x])
                x += 1
        return add_values
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return list based on equality of each item that can be used to filter a Simpy array."""
        eq_values: list[bool] = []
        x: int = 0

        if type(rhs) == float:
            while x < len(self.values):
                if self.values[x] == rhs:
                    eq_values.append(True)
                else:
                    eq_values.append(False)
                x += 1
        else: 
            assert len(self.values) == len(rhs.values)
            while x < len(self.values):
                if self.values[x] == rhs.values[x]:
                    eq_values.append(True)
                else:
                    eq_values.append(False)
                x += 1
        return eq_values
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return list based on the greater value of each item that can be used to filter a Simpy array."""
        gt_values: list[bool] = []
        x: int = 0

        if type(rhs) == float:
            while x < len(self.values):
                if self.values[x] > rhs:
                    gt_values.append(True)
                else:
                    gt_values.append(False)
                x += 1
        else: 
            assert len(self.values) == len(rhs.values)
            while x < len(self.values):
                if self.values[x] > rhs.values[x]:
                    gt_values.append(True)
                else:
                    gt_values.append(False)
                x += 1
        return gt_values
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Read the subscription notation and allows specific values from the values list to be outputed."""
        gotem_values: Simpy = Simpy([])
        x: int = 0

        if type(rhs) == int:
            return self.values[rhs]
        else: 
            while x < len(rhs):
                if rhs[x]:
                    gotem_values.values.append(self.values[x])
                x += 1
            return gotem_values