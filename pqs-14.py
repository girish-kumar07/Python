# Adding elements of two lists
l = [3,1,4]
m = [1,5,9]

n = []

for a,b in zip(l , m):
    n.append(a+b)

print(n)


# Using list comprehension
# n = [a+b for a,b in zip(l,m)]
# print(n)

# Using numpy library
# import numpy as np

# n = (np.array(l)+np.array(m))
# print(n)