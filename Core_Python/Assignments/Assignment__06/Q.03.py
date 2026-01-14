# Q1. Write a program to print the following patterns:

# Pattern (c) – Alphabet Repeating Triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + i), end = ' ')
    print()
