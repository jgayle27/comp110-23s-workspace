"""Practice with dictionaries."""

"""Add mint"""
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print("After adding mint: ")
print(ice_cream)

"""Remove mint"""
ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

"""Accessing, use single quotes with f string"""
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

"""Updating a value"""
ice_cream["vanilla"] += 1
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

"""CHecking if in dictionary"""
print("mint" in ice_cream)
print("chocolate" in ice_cream)