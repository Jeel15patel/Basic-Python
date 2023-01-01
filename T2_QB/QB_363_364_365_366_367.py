# 363 :- Write a Python program to swap first and last element of the list
# 364 :- Write a Python program to find the sum of all the elements in the list. 
# 365 :- Write a Python function to sum all the numbers in a list
# 366 :- Write a Python program of Reversing a List.
# 367 :- Write a Python program to Merging two Dictionaries

l = [12,45,67,89,123]
print("Orinal List",l )
for i in l:
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
print("Swap first and last element",l)  

print("-----364-&-365-----")

l = [12,45,67,89,123]
sum = 0
for i in range(len(l)):
    sum = sum + l[i]
print(sum)

print("--------366--------")

list1 = [12,45,67,89,123]
list2 = list1[::-1]
print("Reversing a List",list2)

print("--------367--------")

dict_1 = {1: 'J', 2: 'e'}
dict_2 = {3: 'l', 4: 'p'}

print(dict_1 | dict_2)

"""def Merge(dict1, dict2):
	return(dict2.update(dict1))

dict1 = {'w': 5, 'x': 10}
dict2 = {'y': 15, 'z': 20}

print(Merge(dict1, dict2))
print(dict2)
"""

