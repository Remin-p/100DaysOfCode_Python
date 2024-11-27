'''
Day 23 - List intersection
Write a function to find the intersection of two lists.

Breaking the rules from now on, tired of writing so many functions.
'''
print("Finding the intersection of two lists...")

listA = [1,2,3,4,5,6,7,8,9,10]
listB = [5,6,7,8,9,10,11,12,13,14,15]
intersection = []

for item in listA:
    if(item in listB):
        intersection.append(item)
        
print(intersection)