"""
Day 16 - Palindrome String
Write a function to check if a given string is a palindrome.

USER: Uncharted territory. Never did string manipulation in Python before.
"""

print("Palindrome checker...")

userString = input("Input your string: ")
revString = userString[::-1]

if userString == revString:
    print("{word} is a palindrome.".format(word=userString))
else:
    print("{word} is not a palindrome.".format(word=userString))
