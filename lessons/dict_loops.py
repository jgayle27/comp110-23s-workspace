"""Practice with dictionaries and for loops."""

grades: dict[str, str] = {"Alyssa": "A", "Aksana": "A", "Regis": "B"}

for student in grades:
    print(grades[student])

for student in grades:
    if grades[student] == "A":
        print(f"Yay {student}!")

print(grades["Frank"])
