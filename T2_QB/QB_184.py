# Write a Python program to demonstrate the function of finding sum and average of first n natural numbers.

n = int(input("Enter the NUmber: "))
def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
        avg = sum / i
    return sum,avg
sum,avg = sum(n)
print("Sum=",sum,"Avg",avg)
