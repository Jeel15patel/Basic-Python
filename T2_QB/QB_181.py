# Write a Python program to check whether the given no is Armstrong or not using user defined function. 

def arm(n):
    sum = 0
    tem = n
    while (n != 0):
        x = n % 10
        sum = sum + x * x * x
        n  = n // 10
    if(sum == tem):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
n = int(input("Enter num: "))
arm(n) 


