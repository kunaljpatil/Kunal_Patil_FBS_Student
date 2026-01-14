# Q4. Find Second Largest Number Using Bubble Sort

lst = [12, 5, 18, 7, 11]

# bubble sort
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Second Largest =", lst[-2])
