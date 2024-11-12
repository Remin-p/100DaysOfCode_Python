'''
Day 5 - Conditional Statements
1. (DONE)
2. (DONE)
3. (DONE)
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F) 
'''
print("Grading...")

pcnt = int(input("Insert percentage of grade: "))

print("Calculating grade...")

if(pcnt < 19):
    print("F")
elif(pcnt < 39):
    print("D")
elif(pcnt < 59):
    print("C")
elif(pcnt < 79):
    print("B")
else:
    print("A")
