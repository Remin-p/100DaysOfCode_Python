'''
Day 6 - Calculate the area of a circle.
Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits
'''
import math

pi = math.pi

print("Calculating the area of a circle...")

# 1. Measure the radius (take it from the user)
r = int(input("Insert the circle's radius (Measure the distance from the center of the circle to its edge): "))

# 2. Multiply the radius by itself so you get r²
r = r * r

# 3. Finally, multiply by Pi
area = r * pi

# Since we only want 2 decimal digits...
areaRounded = format(area, ".2f")

print("The area of the circle is:",areaRounded)

# Math is something 