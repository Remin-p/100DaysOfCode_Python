'''
Day 21 - Reverse List
Write a function to reverse a list.
'''
print("Reversing a list...")
userList = [1,2,3,4,5]

def reverseList(list):
    index = 1
    reverseList = []
    for item in list:
        reverseList.append(list[len(list)-1])
    return(reverseList)

# Or I could use the reverse() built-in function. :T
# I will be paying more attention to the official python docs from now one.

print(reverseList(userList))