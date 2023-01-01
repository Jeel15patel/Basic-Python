# Write a Python function to calculate the factorial of a given number.

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
num = int(input("Enter The factorial of Nub: "))
print("Factorial is",fact(num))