# Write a program to calculate the sum and average of the digits present in a string. 

str = input("Enter Text: ")
total = 0
cout = 0 
for i in str:
    if i.isdigit():
        total = total + int(i)
        cout = cout + 1
avg = total / cout
print("Sum is",total,"and Average is",avg )
        
