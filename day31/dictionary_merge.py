'''
Day 31 - Merge dictionaries.
Merge two dictionaries.
'''

dic1 = { "keydict1":"data1" }
dic2 = { "keydict2":"data2" }
joined = {}

joined.update(dic1)
joined.update(dic2)

print(joined)