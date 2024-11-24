"""
Day 19 - Maximum in List
Write a function to find the maximum element in a list.

USER: My first solution was this one, before I realized there is a max() builtin function.
"""

print("Largest element in a list...")

userList = [1, 2, 3, 45, 5, 67, 7, 8, 9, 10]


def largest(uStr):
    largest = 0

    for item in uStr:
        if item > largest:
            largest = item

    return largest


print(largest(userList))
