"""
Day 34 - File operations: Append
Append data to an existing text file.
"""

with open("./file.txt", "r+", encoding="utf-8") as f:
    f.read()
    f.write(
        "...The things that cannot be cut by my Roukanken, forged by Youkai...\nAre close to none!"
    )
