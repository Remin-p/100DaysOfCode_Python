'''
Day 11 - While-loop
Use a while loop to print even numbers from 2 to 20.
'''
print("While loop for even numbers...")
i = 0

while(i < 20):
    if(i % 2 == 0) & (i != 0): 
        print(i) # Initially I did print(i+1) then started wondering why it was printing odd numbers LMAO
    i += 1