# Write a program to find all occuences of a sub string in a given string by ignoring the case.

str = input("Enter The String: ")
sub_str = input("Enter The String you Whant to count: ")
tm = str.lower()
ts = sub_str.lower()
for i in tm:
    count = 0
    if tm == ts:
        count = count + 1
    print(count)