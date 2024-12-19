'''
Day 33 - File operations: Write
1. Write data to a text file.
2. [...]
'''

with open('./file.txt', 'w', encoding='utf-8') as f:
    f.write('From that day forth... my arm changed... and a voice echoed, "Power. Give me more power!" And if I become a demon, so be it. I will endure the exile. Anything to protect her.')
    # f.read()

with open('./file.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()

print(str(file_content))