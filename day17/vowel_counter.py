"""
Day 17 - Number of vowels in a string
Write a function to count the number of vowels in a string.
"""

print("Vowel counter...")

vowels = ["a", "e", "i", "o", "u"]


def vowelCounter(userStr):
    vowelsInStr = 0
    for char in userStr.lower():
        if char in vowels:
            vowelsInStr += 1
    return vowelsInStr


print(vowelCounter(input("Insert your string: ")))  # wacky
