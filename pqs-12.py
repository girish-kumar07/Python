#Finding elements index.
tup = tuple("apple")
print(tup)
char = input("Enter the character without quotes: ")
if char in tup:
    count = 0
    for a in tup:
        if a!= char:
            count = count + 1
        else:
            break

    print(char,"is at position",count,"in",tup)
else:
    print(char,"is NOT in ",tup)