'''
Day 22 - List duplicates
Write a function to remove duplicates from a list.
'''
print("Remove duplicates from a list...")

userList = ["Gon","Killua","Hisoka","Chrollo","Ging","Gon","Illumi","Alluka","Nanika","Killua","Leorio","Kurapika","Is","Now","Drowning","In","An","Indescribable","Emptiness","Take","It","Back","Leorio","You","Take","It","Back","It's","Mr","Leorio"]

def dupeDelete(list):
    return set(list)

print(dupeDelete(userList))