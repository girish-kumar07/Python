def feet_to_inches (feet):
    return  feet * 12

def input_feet ():
    feet = float(input("Enter the feet:- "))
    return feet

def input_inches ():
    inches = float(input("Enter the inches:- "))
    return inches

feet_ = input_feet()
inches_ = input_inches()
result = feet_to_inches(feet_)

print("Feet enterd by user:-",feet_,"\nInches entered by the user:-",inches_,"\nEntered feet into inches=",result)