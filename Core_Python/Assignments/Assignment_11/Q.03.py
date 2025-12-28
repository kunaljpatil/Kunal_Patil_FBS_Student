# Q3. Sort List According to Second Element in Sublist

lst = [[1,5], [4,2], [7,3]]

for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j][1] > lst[j+1][1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted List =", lst)
