"""
Day 18 - List Sum
Write a function to find the sum of all elements in a list.
"""

print("Sum all elements in a list...")
userList = [1, 2, 3, 4, 5]


def sumList(lst):
    itemSum = 0
    for item in lst:
        itemSum += item
    return itemSum


print(sumList(userList))
