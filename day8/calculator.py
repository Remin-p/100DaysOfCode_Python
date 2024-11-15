'''
Day 8 - Simple Calculator
Create a simple calculator program that can add, subtract, multiply, and divide two integers

USER: Easy peasy!
'''
print("Calculator...")

select = ''
options = ["add","sub","mul","div"]
n1 = int(input("Input the 1st number..."))
n2 = int(input("Input the 2nd number..."))

while(select not in options):
    select = input("Would you like to:\n (add), (sub)tract, (mul)tiply or (div)ide?\n")

def add():
    print(n1+n2)
def sub():
    print(n1-n2)
def mtp():
    print(n1*n2)
def dvd():
    print(float(n1/n2))

if(select == "add"): 
    add()
if(select == "sub"):
    sub()
if(select == "mul"):
    mtp()
if(select == "div"):
    dvd()
if(select not in options):
    print("you breached containment")