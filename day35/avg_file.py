"""
Day 35 - File operations
Calculate the average of numbers in a text file.
"""

with open("./file.txt", "r") as f:
    file_content = f.read()

allSum = 0

for num in file_content.split():
    allSum += int(num)

avg = float(allSum / len(file_content.split()))

print(avg)
