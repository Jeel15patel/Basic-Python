# Write a Python program to find reverse of given number using user defined function. 

def rev(n):
    rev_num = 0
    
    while n != 0:
        digit = n % 10
        rev_num = rev_num * 10 + digit
        n //= 10
    print("Reverse is ",rev_num)
    
n = int(input("Enter The Reverse Number: "))    
rev(n)

