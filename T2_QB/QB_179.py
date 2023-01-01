#  Write a Python function to find the Max of TWO numbers.

def max(a,b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter A:"))
b = int(input("Enter B:"))
print("MAX: ",max(a,b))