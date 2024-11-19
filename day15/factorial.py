"""
Day 15 - Factorial
Write a function to calculate the factorial of a number.

USER: And finally, functions!
"""

import math

print("Calculate factorial...")

numIn = int(input("Input number to calculate factorial of:"))


def factorio(num):
    fct = 1
    while num > 0:
        fct *= num
        print(num, "factorial:", fct)
        num -= 1


factorio(numIn)
