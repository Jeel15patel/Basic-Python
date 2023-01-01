# 247 :- Write a program to reverse a given string 
# 248 :- Write a Python program to print even length words in a string

str = input("Enter String : ")
str2 = str[::-1]
print("The reverse is",str2)

str = input("Enter String : ")
split_s = str.split(" ")
for i in split_s:
    if len(i) % 2 == 0:
        print(i)