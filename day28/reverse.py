'''
Day 28 - Reverse words
Reverse words in a sentence.
'''

sentence = "Kurapika is now drowning in an indescribable emptiness"
words = sentence.split()
ecnetnes = ''

for word in words:
    ecnetnes += ''.join(reversed(word)) + ' ' 

print(ecnetnes)