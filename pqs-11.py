line = input("Enter the line:- ")
lower_count = upper_count = 0
digit_count = alpha_count = 0
for a in line:
    if a.islower():
        lower_count += 1
    elif a.isupper():
        upper_count += 1
    elif a.isdigit():
        digit_count += 1 
    if a.isalpha():
        alpha_count += 1

print("Numbr of upper case letters:- ",upper_count)
print("Number of lower case letters:- ",lower_count)
print("Number of alphabets:- ",alpha_count)
print("Number of digits:- ",digit_count)