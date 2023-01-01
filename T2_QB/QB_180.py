# Write a Python program to accept two numbers and check it for odd or even number

def eveodd(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
n = int(input("Enter The Value: "))
eveodd(n)