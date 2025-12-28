# Q1. Write a program to print the following patterns:

# Pattern (b) – Alphabet Increasing Triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + j), end = ' ')
    print()
