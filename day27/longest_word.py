'''
Day 27 - Longest word
Find the longest word in a sentence.
'''

sentence = "O believe! You were not born for no reason, have not lived for nothing, nor have suffered in vain. What was born must also die. What was dead shall rise again, so tremble no more; and prepare yourself to live! with wings that I have won for myself, in a striving for love, I shall soar up to the light which no eyes have ever seen! I shall die as so to live."
words = sentence.lower().split()
longest = ""

# Cleaning up special characters
for word in words:
    word = word.removesuffix(":")
    word = word.removesuffix(",")
    word = word.removesuffix("!")
    word = word.removesuffix(".")
    word = word.removesuffix(";")

    if(len(word) >= len(longest)):
        longest = word

print(longest) 
