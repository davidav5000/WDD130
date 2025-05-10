import math

# old code for reference
# lengthsq =input("What is the lenght of the side of the square in centemeters? ")
# lenghtsq_input = int(lengthsq)
# areasquare = lenghtsq_input **2
# print(f"The area of the square is: {areasquare}") 
# volumecube = lenghtsq_input **3
# print(f"The volume of the cube is: {volumecube}") 
# lengthrec =input("\nWhat is the lenght of the of the rectangle in centemeters? ")
# widthrec =input("\nWhat is the width the of the rectangle in centemeters? ")
# widthrec_input = int(widthrec)
# lengthrec_input = int(lengthrec)
# arearec = lengthrec_input * widthrec_input
# print(f"\nThe area of the rectangle is: {arearec}")
# radius =input("What is the radius of the circle in centemeters? ")
# radius_input = float(radius)
# shpere_volume = (4/3) * math.pi * radius_input **3
# areacir = radius_input **2 * math.pi
# print(f"\nThe area of the circle is: {areacir}")
# print(f"\nThe volume of the sphere is: {shpere_volume}")


lengthsq =input("What is the lenght of the side of the square in centemeters? ")
lenghtsq_input = float(lengthsq)
areasquare = lenghtsq_input / 100 
sqcm = lenghtsq_input **2
print(f"\nThe area of the square is: {sqcm}cm") 
sqm = areasquare **2
print(f"The square meter of the square is: {sqm:.4f}m")
volumecube = lenghtsq_input **3
print(f"The volume of the cube is: {volumecube}") 
#Cube^^^
lengthrec =input("\nWhat is the length of the of the rectangle in centemeters? ")
widthrec =input("\nWhat is the width the of the rectangle in centemeters? ")
lengthrec_input = float(lengthrec)
widthrec_input = float(widthrec)
arearec = lengthrec_input * widthrec_input
lengthrecm = lengthrec_input / 100
widthrecm = widthrec_input / 100
recsqm = lengthrecm * widthrecm
print(f"\nThe area of of the rectangle is: {arearec:.4f}cm")
print(f"The square meter of the rectangle is: {recsqm:.4f}m")
#Rectangle^^^
radius =input("\nWhat is the radius of the circle in centemeters? ")
radius_input = float(radius)
radiuscm = radius_input / 100
sphere_volume = (4/3) * math.pi * radius_input **3
areacirm = radiuscm **2 * math.pi
print(f"\nThe area of the circle is: {areacirm:.4f}m")
print(f"The volume of the sphere is: {sphere_volume:.4f}")
#Circle^^^