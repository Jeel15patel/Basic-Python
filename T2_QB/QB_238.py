# Write a Python program to check if a string is palindrome or not.

def pro(s):
    s2 = s[::-1]
    if s2 == s:
        print("This String is palindrome")
    else:
        print("This String is NOT palindrome")
s = input("Enter String: ")
pro(s)