# Q1. Write a program to print the following patterns:

# Pattern (f) – Symmetric Number Pyramid

n = 5
for i in range(1, n +1 ):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(j-1, 0, -1):
        print(k, end = "")
    print()
