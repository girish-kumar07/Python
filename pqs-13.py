# Checking presence of value inside a dictionary.
info = {'Riya':'CSE','Marks':'100','Ishpreet':'Eng','Kamaal':'Env.Sc'}
val = input("Enter the value to be searched:- ")
if val in info.values():
    for a in info:
        if info[a] == val :
            print("The key of given value is:- ",a)
            break
else:
    print("Given value does not exist in Dictionary")