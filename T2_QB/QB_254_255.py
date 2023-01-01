# 245 :- Write any program to demonstrate Tuples in Python 
# 255 :- Write a Python program to demonstrate the slicing of a Tuple

# Different types of tuples
# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

print("--------------255--------------")

my_tuple = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = my_tuple[3:5]
print(_slice)

_slice = my_tuple[:6]
print(_slice)

_slice = my_tuple[6:]
print(_slice)

_slice = my_tuple[-3:-5]
print(_slice)

_slice = my_tuple[:-2]
print(_slice)

_slice = my_tuple[::-1]
print(_slice)

_slice = my_tuple[::4]
print(_slice)

_slice = my_tuple[9:2:4]
print(_slice)