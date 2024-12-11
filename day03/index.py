'''
Day 3 - Input and Output
1. Write a program that reads user input and print it to the console.
2. Modify the program to read and print different data type inputs (integers, floating-point numbers, strings)
'''

userName = input("Input your name:")
userAge = int(input("Input your age:"))
userFingers = int(input("Input how many fingers you have:"))
userPi = float(input("Input as many digits of Pi as you can remember (example: 3.1415)"))
userQuestion = input("Are you missing any fingers now? (y/n)")

if(userQuestion == "y"):
    userQuestion = True
elif(userQuestion == "n"):
    userQuestion = False
else:
    userQuestion = 'undefined'

print('''
User info:
Name: {name}
Age: {age}
Fingers: {fingers}
Pi digits: {pidig}
Is missing fingers after proccess: {missing}
'''.format(
    name=userName,
    age=userAge,
    fingers=userFingers,
    pidig=userPi,
    missing=userQuestion
))