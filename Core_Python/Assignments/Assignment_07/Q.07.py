# Q1. Write a program to print the following patterns:

# (g) Pyramid of X Characters


for i in range(1, 6):
    for j in range(1, i +1):
        print('X', end = '')
        print(' ', end = '')
    print()

for i in range(4, 0, -1):
    for j in range(1, i +1):
        print('X', end = '')
        print(' ', end = '')
    print()
