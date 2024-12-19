"""
Day 33 - File operations: Write
1. Write data to a text file. (DONE)
2. Make a function to read and to write content that has been input by the user to a text file.
"""

import io


def writeFile(usrInput):
    with io.open("./userFile.txt", "w", encoding="utf-8") as f:
        f.write(usrInput)

    with io.open("./userFile.txt", "r", encoding="utf-8") as f:
        file_content = f.read()

    return file_content


print("Content written to file:", writeFile(input("Insert content of the file:\n")))
