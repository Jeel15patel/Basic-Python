# 251 :- Write a program to Create a string made of the middle three characters
# 253 :- Write a program to Split a string on hyphens

a = input("Enter String: ")
l = len(a)
mid = l // 2
x = a[mid-1 : mid+2]
print("The middle three characters is:-",x)


str = input("Enter String: ")
sp = input("Enter thing you want to split string:  ")
str_split = str.split(sp)
for i in str_split:
    print(i)


