# Write a Python function to display the Fibonacci sequence till the given user input n.

# kuY66YNZw66@n.C 

n = int(input("Enter the number Fibonacci :"))

def fib(n):
    n1 = 0
    n2 = 1
    if n < 0:
        print("Enter The Positive Number")
    elif n==1:
        print("Fibonacci sequence First Term:",n1)
    else:
        print("Fibonacci sequence is:")
        print(n1)
        print(n2)
        for i in range(n-2):
            nth = n1 + n2
            print(nth)
            n1=n2
            n2=nth
fib(n)