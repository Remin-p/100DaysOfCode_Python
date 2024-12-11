'''
Day 5 - Conditional Statements
1. (DONE)
2. Write a program that takes three numbers as input and prints the largest among them
3. Write a program that checks if a given input year is a leap year or not
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F) 
'''
print("Check largest number...")


num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))
num3 = float(input("Enter the 3rd number:"))

if(num1 > num2) & (num1 > num3):
    print("The 1st number is the largest number: {n}".format(n=num1))
if(num2 > num1) & (num2 > num3):
    print("The 2nd number is the largest number: {n}".format(n=num2))
if(num3 > num1) & (num3 > num2):
    print("The 3rd number is the largest number: {n}".format(n=num3))
