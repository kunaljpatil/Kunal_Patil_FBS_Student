# Q1. Write a program to print the following patterns:

# (e) Powers of 11 (Pascal-like Triangle)

n = 4

for i in range(0, n):
    print(" " * (n - i - 1), end="")
    print(11 ** i)
