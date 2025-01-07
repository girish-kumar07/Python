list = []

list.append(input("Enter the list DATA:- "))
list.append(input("Enter the list DATA:- "))
list.append(input("Enter the list DATA:- "))
list.append(input("Enter the list DATA:- "))

list_copy = list.copy()
list_copy.reverse()

if(list_copy == list):
    print("Entered list is Palindrome")
else:
    print("Entered list in Not Palindrome")