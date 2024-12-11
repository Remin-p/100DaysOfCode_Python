'''
Day 5 - Conditional Statements
1. (DONE)
2. (DONE)
3. Write a program that checks if a given input year is a leap year or not
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F) 
'''
print("Check if leap year...")

year = int(input("Insert year: "))
isLeap = None

if(year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)):
    isLeap = True

if(isLeap != True):
    print("{yr} is not a leap year.".format(yr=year))
else:
    print("{yr} is a leap year.".format(yr=year))