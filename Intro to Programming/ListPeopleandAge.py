
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
young_age = 100
young_name = ""

for line in people:
    parts = line.split()
    name = parts[0]
    age = int(parts[1])

    if age < young_age:
        young_age = age
        young_name = name

print(f"The youngest person: {young_name}\nYoungest Age: {young_age}")
