# Q1. Write a program to find sum of series 1! + 2! + ... + n! using recursion.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def sum_series(n):
    if n == 1:
        return 1
    else:
        return fact(n) + sum_series(n - 1)

num = int(input("Enter n: "))
print("Sum of series =", sum_series(num))
