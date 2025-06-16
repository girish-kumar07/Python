pound = int(input("Enter the Pounds:- "))
print("Pounds\tKilograms")
print("------------------")

for i in range(1,pound+1):
    kilogram = i * 0.453
    print(i,"\t",kilogram)