# Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters

def upwldl(n):
    ul = 0
    wl = 0
    dl = 0
    for i in n:
        if i.isupper():
            ul = ul + 1
        elif i.islower():
            wl = wl + 1
        elif i.isdigit():
            dl= dl + 1 
    print("Total Number of Upper Letter is",ul)
    print("Total Number of Lower Letter is",wl)
    print("Total Number of Digit Letter is",dl)
s = input("Enter The String: ")
upwldl(s)