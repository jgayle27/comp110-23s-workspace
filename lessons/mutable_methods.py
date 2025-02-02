


from __future__ import annotations

class Point:
    """Model a 2D point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with its x,y coponents"""
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y*factor)
        return(scaled)
    
    def __str__(self):
        """Print prettier version of out point."""
        return f"({self.x},{self.y})"
    
    def __mul__(self, factor: float) -> float:
        scaled: Point = Point(self.x * factor, self.y*factor)
        return(scaled)
    
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation."""
        if index == 0:
            return self.x
        else:
            if index == 1:
                return self.y
            else: 
                raise IndexError
    
a: Point = Point(1.0, 2.0)
#b: Point = a.scale(3.0)
b: Point = a * 3.0
# print(str(a))
# print(a)
print(b)
print(f"My point is {b}")
print(b[1]) # gives y-coordinate, b[0] is x-coordinate

