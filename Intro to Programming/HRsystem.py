with open("C:/Users/David/OneDrive/WDD130/Intro to Programming/hr_system.txt") as HR:
    for line in HR:
        hrlist = line.split()
        name = hrlist[0]
        title = hrlist[2]
        id = hrlist[1]
        salary = float(hrlist[3])
        print(f"{name} (ID {id}), {title} - ${salary:.2f}")