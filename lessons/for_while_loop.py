""""""

"""while loop."""
idx: int = 0
xs: list[int] = [1,2,3]
while idx < len(xs):
    elem: int = xs[idx]
    print(elem)
    idx+=1


"""More concise way to write the same thing -> a "for loop"."""
for elem in xs:
    print(elem)

"""Example 2:"""
cats: list[str] = ["Stinky", "Felicia", "Toulouse", "Skippy"]

for praise in cats:
    print(f"Good kitty, {praise}!")

"""using range"""
names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0,3):
    print(f"{idx}: {names[idx]}")
    