# List of miltiple of 3 and 5 under entered number.
n = int(input("Enter the number:- "))
lst = []
for i in range(0,n+1):
    if i%3==0 or i%5==0:
        lst.append(i)

print(lst)