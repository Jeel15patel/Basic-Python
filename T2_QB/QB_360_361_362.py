# 360 :- Write a Python program to print the even numbers from a given list
# 361 :- Write a Python Program to print the largest even number in a list. 
# 362 :- Write a Python Program to print the largest odd number in a list.

l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i % 2 == 0:
        print(i)
    else:
        pass
    
print("-------361-&-362-------")

l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    if l[i] % 2 == 0:
        maxe = l[i]
    if l[i] % 2 == 1:
        maxo = l[i]
    
for i in range(len(l)):
    if l[i] >= maxo and l[i] % 2 == 0:
            maxe = l[i]
    if l[i] >= maxo and l[i] % 2 == 1:
        maxo = l[i]

print("Odd Max:- ",maxo)
print("Even Max:- ",maxe)