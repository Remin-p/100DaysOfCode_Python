'''
Day 26 - Anagram strings
Write a function check if two strings are anagrams.
'''

str1 = "ama grana"
str2 = "anagrama"

# Sorts all characters, replaces all whitespace, then compares the two strings.
if(sorted(str2.replace(" ", "")) == sorted(str1.replace(" ", ""))):
    print(str1,"is an anagram of",str2)