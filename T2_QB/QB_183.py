# Write a Python Program to demonstarte a Simple Calculator using python functions

def cal(c):
    
    if c == "+":
        print("ADD:",a + b)
        
    elif c == "-":
        print("SUB:",a - b)
        
    elif c == "*":
        print("MUL:",a * b)
        
    elif c == "/":
        print("DIV:",a / b)
        
    elif c == "%":
        print("F_DIV:",a % b)
        
    else:
        print("Select correct sing")

a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
c = input("Option: \n ADD :- + \n SUB :- - \n MUL :- * \n DIV :- / \n F_DIV :- // \n Cose \n Select: ")
cal(c)