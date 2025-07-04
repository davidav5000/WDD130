years =[]
ages = []
countries =[]
abvs =[]
life_exp = ""
with open("C:/Users/David/OneDrive/WDD130/Intro to Programming/life-expectancy.csv") as LIFE:
    next(LIFE)
    for line in LIFE:
        parts = line.strip().split(",")
        countries.append(parts[0])
        abvs.append(parts[1])
        years.append(int(parts[2]))
        ages.append(float(parts[3]))

life_exp = (min(ages))
print(f"The min life expectancy {life_exp}")
life_exp = (max(ages))
print(f"The max life expectancy {life_exp}")

