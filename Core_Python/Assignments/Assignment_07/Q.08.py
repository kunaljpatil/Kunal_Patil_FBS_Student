# Q1. Write a program to print the following patterns:

# (h) Number Pattern with Conditional Spaces
for i in range(1, 6):
    for j in range(1,i +1):
        if ((i == 3 and j == 2) or (i == 4 and j == 2) or (i == 4 and j == 3)):
            print(' ', end = ' ')
        else:
            print(j, end = ' ')
    print()
