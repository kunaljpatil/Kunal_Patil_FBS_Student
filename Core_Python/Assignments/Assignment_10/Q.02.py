# Q2. Write a program to find maximum and minimum element in a list.

lst = [4, 9, 2, 11, 6]

maxi = lst[0]
mini = lst[0]

for x in lst:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

print("Maximum =", maxi)
print("Minimum =", mini)
