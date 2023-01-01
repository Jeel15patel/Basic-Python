# Write a program to create a string made of first,middle and last character.

str = input("Enter The String: ")
l = len(str)
start_l = str[0]
last_l = str[-1]
mid_v = int(l/2)
mid_l = str[mid_v]
print("The First + MID + LAST is",start_l + mid_l + last_l)
