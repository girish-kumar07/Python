miles = int(input("Enter the miles:- "))
print("Miles\tKilometer")
print("------------------")
for i in range(0,miles):
    kilometer = i * 1.609
    i = i+1
    print(i,"\t",kilometer)