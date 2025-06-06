import math
print("Welcome to the velocity calculator. Please enter the following values:\n----------------------------------------------------------------------")
mass = input("Mass (in kg): ")
gravity = input("Gravity (in 9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): ")
time = input("Time (in seconds): ")
density = input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ")
cross = input("Cross-sectional area (in m^2): ")
drag = input("Drag constant (0.5 for square, 1.1 for cylinder): ")
mass = float(mass)
gravity = float(gravity)
time = float(time)
density = float(density)
drag = float(drag)
cross = float(cross)
c = (1 / 2) * density * drag * cross
velocity = math.sqrt((mass * gravity) / c ) * (1 - (math.exp((-math.sqrt(mass * gravity * c) / mass) * time)))
print (f"\nThe inner value of c is: {c:.3f} kg/m^2")
print (f"The velocity of the object after {time:.1f} seconds is: {velocity:.3f} m/s")