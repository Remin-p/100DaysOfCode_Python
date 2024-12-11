'''
Day 5 - Conditional Statements
1. Write a program that reads an integer as user input and prints whether the number is Odd or Even to the console
2. Write a program that takes three numbers as input and prints the largest among them
3. Write a program that checks if a given input year is a leap year or not
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F) 
'''
print("Check if a number is odd or even...")

num = int(input("Input number:"))

if(num % 2 == 0):
    print("Number {n} is even.".format(n=num))
else:
    print("Number {n} is odd.".format(n=num))

# Test if this works as intended.

def test(i):
    for i in range(i+1):
        if(i % 2 == 0):
            print("Number {n} is even.".format(n=i))
        else:
            print("Number {n} is odd.".format(n=i))


allNums = input("Would you like to check which numbers between 0 and {n} are odd/even? (y/N) ".format(n=num))

if(allNums == "y"):
    test(num)
