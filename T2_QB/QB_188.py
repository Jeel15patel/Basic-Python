# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def chk(n):
    l = len(n)
    ul = 0
    wl = 0
    for i in n:
        if i.isupper():
            ul = ul + 1
        elif i.islower():
            wl = wl + 1
    print("Number of String is",l)
    print("Number of Upper Letter is",ul)
    print("Number of Lower Letter is",wl)
n = input("Enter the String: ")
chk(n)