# Q6. Write a program to print Fibonacci series using recursion.

def fib(n):
    if n == 1 or n == 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)

num = int(input("Enter n terms: "))
for i in range(1, num + 1):
    print(fib(i), end=" ")


