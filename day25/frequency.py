'''
Day 25 - Words frequency
Write a function to count the frequency of words in a sentence.
'''
print("Word frequency...")

sentence = "Kurapika: Take that back, Leorio! You take it back. \n Leorio: It's Mr. Leorio."
words = sentence.split()
cleanedWords = []
frequency = {}

# First, clean up the words (so that the special characters aren't treated as part of the words)
for word in words:
    word = word.removesuffix(":")
    word = word.removesuffix(",")
    word = word.removesuffix("!")
    word = word.removesuffix(".")
    cleanedWords.append(word)

# Then, print the frequency of each word, as well as the whole sentence.
for word in cleanedWords:
    if(word not in frequency):
        frequency[word] = cleanedWords.count(word)
        
print(frequency)

''' Expected output:
{
'Kurapika': 1, 
'Take': 1,
'that': 1, 
'back': 2, 
'Leorio': 3, 
'You': 1, 
'take': 1, 
'it': 1, 
"It's": 1, 
'Mr': 1
}
'''