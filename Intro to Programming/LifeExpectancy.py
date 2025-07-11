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


search = int(input("Enter Year of Interest: "))
max_life = -1
max_country = ""
max_abv = ""

total_life = 0
count = 0
min_life = float('inf')
min_country = ""
min_abv = ""

for i in range(len(years)):
    if years[i] == search:
        # Max
        if ages[i] > max_life:
            max_life = ages[i]
            max_country = countries[i]
            max_abv = abvs[i]
        # Min
        if ages[i] < min_life:
            min_life = ages[i]
            min_country = countries[i]
            min_abv = abvs[i]
        # Average
        total_life += ages[i]
        count += 1

if count == 0:
    print(f"No data available for {search}")
else:
    average_life = total_life / count
    print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {search}")
    print(f"\nFor the year {search}:")
    print(f"The average life expectancy across all counties was {average_life:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}")


# life_exp = (min(ages))
# print(f"The min life expectancy {life_exp}")
# life_exp = (max(ages))
# print(f"The max life expectancy {life_exp}")