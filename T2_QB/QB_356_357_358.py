# 356 :- Write a python code to demonstrate any three methods of list 
# 357 :- Write a python code to explain map in Python program. 
# 358 :- Write a python code to explain filter in Python program.

# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)

List = [1, 2, 3, 4, 5]
print(sum(List))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List = [1, 2, 3, 4, 5]
List.reverse()
print(List)

print("----------------357------------")

l=[1,2,3,4,5]
def doubleIt(x):
    return 2*x
l1=list(map(doubleIt,l))
print(l1)

print("----------------358------------")

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

l = [0,5,10,15,20,25,30]
l1 = list(filter(isEven,l))
print(l1)