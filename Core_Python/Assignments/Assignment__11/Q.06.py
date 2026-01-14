# Q6. Find the Union of Two Lists (no duplicates)

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

union = lst1[:]   # copy

for x in lst2:
    found = False
    for y in union:
        if x == y:
            found = True
            break
    if found == False:
        union = union + [x]

print("Union =", union)
