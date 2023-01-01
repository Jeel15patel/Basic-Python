# 368 :- Write a Python program for Words Frequency in String Shorthands.
# 369 :- Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
# 370 :- Write a Python program to rearrange positive and negative numbers in a given array using Lambda.


str = 'Hi there Will, how are you Will, Will you say Hi to me'

my_result = { key: str.count(key) for key in str.split() }

print("The word frequency is : ",my_result)

print("------369------")

list1 = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9,10,-10]
psum = 0
nsum = 0
for i in range(len(list1)):
    if list1[i] > 0:
        psum = psum + list1[i]
    elif list1[i] < 0:
        nsum = nsum + list1[i]
print(psum)
print(nsum)

print("------370------")