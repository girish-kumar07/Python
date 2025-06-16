miles = int(input("Enter the miles:- "))
print("Miles\tKilometer")
print("------------------")
for i in range(1,miles+1):
    kilometer = i * 1.609
    # i = i+1
    print(i,"\t",kilometer)