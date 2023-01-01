# 249 :- Write a Python program to Uppercase Half String from the given string. 
# 250 :- Write a Python program to capitalize the first and last character of each word in a string


s = input("Enter String: ")
a = s.split()
res = []
for i in a:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print(res)


str = input("Enter String: ")
l = len(str)
hf = l // 2
res = ""
for i in range(l):
    if i >= hf:
        res += str[i].upper()
    else:
        res += str[i]
print("The Uppercase Half String is",res)