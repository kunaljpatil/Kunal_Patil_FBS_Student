# Q2. Merge Two Lists and Sort it

lst1 = [8, 3, 1]
lst2 = [7, 2, 9]

merge = lst1 + lst2

# simple bubble sort
for i in range(len(merge)):
    for j in range(len(merge)-1):
        if merge[j] > merge[j+1]:
            merge[j], merge[j+1] = merge[j+1], merge[j]

print("Merged and Sorted List =", merge)


