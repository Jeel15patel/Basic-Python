# 239 :- Write a Python program to Find length of a string in python.
# 240 :- Write a Python function to find length of a string in python without using len function.

def flin(n):
    l = len(n)
    print("The length of String is",l)
s = input("Enter The String: ")
flin(s)

def stlen(s):
    sl = 0
    for i in s:
        sl = sl + 1
    print("The length of String is",sl)
s = input("Enter The String: ")
stlen(s) 