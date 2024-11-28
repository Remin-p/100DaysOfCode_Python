'''
Day 24 - Words to sentence.
Write a function to convert a list of words into a sentence.
'''

wordList = ["Kurapika","is","now","drowning","in","an","indescribable","emptiness."]
sentence = ""

for word in wordList:
    sentence += word + " "

print(sentence)