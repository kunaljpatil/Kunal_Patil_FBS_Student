# Q1. Write a program to print the following patterns:

# Pattern (g) – Hollow Diamond
n = 4
# Upper hollow pyramid
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

# Lower hollow pyramid
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()
