"""
Day 20 - Fibonacci sequence
Write a function to calculate the Fibonacci sequence up to a certain limit.

USER: Now it's getting interesting.
"""

print("Fibonacci sequence...")

limit = int(input("How many times do you want to calculate the fibonacci sequence? "))

# Breaking the limits. Do not do this at home!
# import sys
# sys.set_int_max_str_digits(9999999) # This almost killed my computer as I tried to calculate the fib sequence 100,000,000 times.
# Seriously, if you don't have the hardware to spare, do NOT do this at home!


def fib(limit):
    n1, n2 = 0, 1

    for num in range(limit):
        n1 = n1 + n2
        n2 = n1 + n2

    if limit % 2 == 0:
        return n1
    else:
        return n2


print(fib(limit))
