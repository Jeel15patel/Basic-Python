# 256 :- Write a program to print maximum and minimum elements in given Tuple.
# 257 :- Write a Program to print even numbers from given Tuple.
# 258 :- Write a program to print sum of even numbers and sum of odd numbers from elements given in tuple. 

my_tup = (1,32,456,3415,56,23,4,67,2,0)
max = my_tup[0]
min = my_tup[0]
for i in my_tup:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)

print("--------257-----------")

my_tup = (1,32,456,3415,56,23,4,67,2,0)
for i in my_tup:
    if i % 2 == 0:
        print(i)
        
print("--------258-----------")

my_tup = (1,2,3,4,5,6,7,8,9,10)
cout_e = 0
cout_o = 0
for i in my_tup:
    if i % 2 == 0:
        cout_e = cout_e + 1
    else:
        cout_o = cout_o + 1

print("EVEN sum: ",cout_e)
print("ODD sum: ",cout_o)

