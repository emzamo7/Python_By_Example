#Cylinder Volume
import math
radius = float(input("type the radius please in mts: "))
depth = float(input("type the depth in meters: "))
volume = ((math.pi * radius**2) * depth)
print("the volume is: ")
print(round(volume,3))