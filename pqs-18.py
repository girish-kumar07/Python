# Printing fibonacci series 
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibo_series = []
n = int(input("Enter the number of terms:- "))
for i in range(n):
    fibo_series.append(i)
    
fibonacci_series = tuple(fibo_series)
print("Fibonacci series of",n,"terms is:- ",fibonacci_series)