'''
Day 9 - Random number generator
1. Write a program that generates a random number. 
2. Write a program that generates random number between 2 integers

USER: Again, these could easily be two different functions.
'''
import random
print("Random number generator...")

def rng():
    print(random.random())

def rngIntRange(n1,n2):
    print(random.randint(n1,n2))

rng()
rngIntRange(10,5000)

# Easier than I expected.