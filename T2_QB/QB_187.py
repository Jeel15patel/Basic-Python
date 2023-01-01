# Write a Python function that checks whether a passed string is palindrome or not

def palstr(s):
    s2 = s[::-1]
    if s == s2:
        print("The string are same")
    else:
        print("The string are NOT Same")
s = input("Enter String :-")
palstr(s)


"""def check(s):
    str = ""
    for i in s:
        str = i + str
    if str == s:
        print("The string Same")
    else:
        print("The string Not Same")
s = input("Enter String :-")
print(check(s))"""