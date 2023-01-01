# Write a Python function to check whether a number is in a given range

n = int(input("Enter Number you Find: "))
stn = int(input("Enter Number you START Number: "))
edn = int(input("Enter Number you END Number: "))

def chek(n,stn,edn):
    if(n > stn and n < edn):
        print("YEss")
    else:
        print("No")

chek(n,stn,edn)
    