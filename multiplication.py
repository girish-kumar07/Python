# Multiplication of two digits without using multiplication operator.
n1 = int(input("Enter the first number:- "))
n2 = int(input("Enter the second number:- "))
product = 0
count = n1 
while count>0:
    product = product + n2
    count = count - 1
print("The product of given two numbers is:- ",product)