n = int(input("Enter the numnber:-"))
total = 0

if n>=0:
    start = n
    end = 2*n
else:
    start = 2*n 
    end = n

for i in range(start,end + 1):
    total = total + i

print(total)