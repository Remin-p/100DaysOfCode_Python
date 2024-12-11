'''
Day 4 - Arithmetic Operations
1. [...]
2. Write a program that calculates the area of a rectangle. Prompt the user to input the length(integer) and width(integer) of the rectangle, calculate the area (length * width), and print the result.
3. Modify the above program to read decimal numbers as the length and width, and output the area to two decimal points
'''
# Program 2
print("Calculating the area of a rectangle...")
length = float(input("Input the length of the rectangle:"))
width = float(input("Input the width of the rectangle:"))
area = length * width

print("Area of the rectangle: {:.2f}".format(area))