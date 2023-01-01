# Create a pair of functions to convert Fahrenheit to Celsius temperature values and vice versa. Where C = (F - 32) * (5 / 9) 


print("1:- Fahrenheit to Celsius \n 2:- Celsius to Fahrenheit")

cho = int(input("Enter Your Choice:- "))

def cel():
    f = float(input("Enter The Fahrenheit :"))
    c = (f - 32) * (5 / 9)
    print("The convert of Fahrenheit to Celsius is",c)
    
def fel():
    c = float(input("Enter The Celsius :"))
    f = ((9 / 5)*c)+32
    print("The convert of Celsius to Fahrenheit is",f)
    
if cho==1:
    cel()
elif cho==2:
    fel()
else:
    print("Select 1 Or 2")
    
