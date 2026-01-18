# Q6. Write a program to remove duplicates from the list.

lst = [2, 4, 2, 5, 4, 7, 7]
unique = []

for x in lst:
    found = False
    for y in unique:
        if x == y:
            found = True
            break
    if found == False:
        unique = unique + [x]

print("List without duplicates =", unique)
