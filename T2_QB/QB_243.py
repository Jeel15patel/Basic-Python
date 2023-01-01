# Write a program to remove I'th character from string in python.

String = input("Enter The String: ")
new_st = ""
Remove_S = int(input("Enter Remove Number: "))
for i in range(len(String)):
    if i != Remove_S:
        new_st = new_st + String[i]
print("The String From Removeing elemt:-",new_st) 