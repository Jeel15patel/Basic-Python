# Write a Python program to demonstrate the function of finding multiplication of first n natural numbers.

n = int(input("Enter the NUmber: "))
def mul(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul * i
        avg = mul / i
    return mul,avg
mul,avg = mul(n)
print("Mul=",mul,"Avg",avg)