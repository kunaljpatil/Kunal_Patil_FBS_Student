# Q1. Write a program to print the following patterns:

# Pattern (e) – Number Pyramid

n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        print(j, end="")
    print()
