# Swapping of two words using third variable.
first = input("Enter the first word:- ")
second = input("Enter the second word:- ")

print("Before swapping, variable first=",first)
print("Before swapping, variable second=",second)
third = first
first = second
second = third
print()
print("After swapping, variable first=",first)
print("After swapping, variable second=",second)